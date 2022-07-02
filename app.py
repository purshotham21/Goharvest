# Store this code in 'app.py' file
  
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from service import farmingService, farmingRepository

import MySQLdb.cursors
import re
import json

  
app = Flask(__name__)
  
  
app.secret_key = 'mysecret'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'agriculture'
  
mysql = MySQL(app)
  
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    sellingprices = []
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = % s AND password = % s', (email, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['uuid'] = account['uuid']
            session['name'] = account['name']
            session['email'] = account['email']
            print('Login Successful')
            return redirect(url_for('dashboard'))
        else:
            msg = 'Incorrect email / password !'
    return render_template('login.html', msg = msg)
  
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('uuid', None)
    session.pop('name', None)
    session.pop('email', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if session.get('loggedin'):
        sellingprices = farmingRepository.getSellingPrices()
        print(sellingprices)
        userId = session['uuid']
        analytics = farmingRepository.getAnalytics(userId);
        for i in range(len(analytics)):
            intake = json.loads(analytics[i].get('intake'))
            results = json.loads(analytics[i].get('results'))
            analytics[i].update({'intake':intake})
            analytics[i].update({'results':results})
        print("------------------------------------------------------")
        print(analytics)
        latestAnalytics = farmingRepository.getLatestAnalytics(userId);
        if(latestAnalytics):
            latestAnalytics = json.loads(latestAnalytics[0].get('results'))
        else:
            latestAnalytics = {}
        print("------------------------------------------------------")
        print(latestAnalytics)
        print(type(latestAnalytics))
        return render_template('index.html',sellingprices = sellingprices, analytics = analytics, latestAnalytics = latestAnalytics)
    else:
        return redirect(url_for('login'))

@app.route('/intelligentFarming')
def intelligentFarming():
    return render_template('input.html')

@app.route('/results')
def results():
    userId = session['uuid']
    results = farmingRepository.getLatestAnalytics(userId);
    results = json.loads(results[0].get('results'))
    return render_template('results.html',results = results)

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', name):
            msg = 'Name must contain only characters and numbers !'
        elif not name or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (name, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    else:
        return render_template('signup.html',msg = msg)
    return redirect(url_for('login'))


@app.route('/runModel', methods =['POST'])
def runModel():
    intake = request.form
    userId = session['uuid']
    crops = intake.getlist('crops')
    sellingPrices = farmingRepository.getCropSellingPrices()
    Dict ={'pct_sc1': int(intake.get('pct_sc1')),
       'pct_sc2': int(intake.get('pct_sc2')),
       'pct_sc3': int(intake.get('pct_sc3')),
       'total_space': int(intake.get('total_space')),
       'crops': crops,
       'sc1_crop1': int(intake.get('sc1_crop1')),
       'sc1_crop2': int(intake.get('sc1_crop2')),
       'sc1_crop3': int(intake.get('sc1_crop3')),
       'sc2_crop1': int(intake.get('sc2_crop1')),
       'sc2_crop2': int(intake.get('sc2_crop2')),
       'sc2_crop3': int(intake.get('sc2_crop3')),
       'sc3_crop1': int(intake.get('sc3_crop1')),
       'sc3_crop2': int(intake.get('sc3_crop2')),
       'sc3_crop3': int(intake.get('sc3_crop3'))}
    print(Dict)
    crop1 = crops[0]
    crop2 = crops[1]
    crop3 = crops[2]
    crop_sp1 = sellingPrices.get(crop1)
    crop_sp2 = sellingPrices.get(crop2)
    crop_sp3 = sellingPrices.get(crop3)
    Dict.update({'revenue_crop1': crop_sp1})
    Dict.update({'revenue_crop2': crop_sp2})
    Dict.update({'revenue_crop3': crop_sp3})
    results = farmingService.runModel(Dict)
    #save intake and results
    farmingRepository.saveAnalytics(userId, Dict, results)
    return redirect(url_for('results'))
