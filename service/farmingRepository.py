from flask import Flask
from flask_mysqldb import MySQL

import MySQLdb.cursors
import json

app = Flask(__name__)

app.secret_key = 'mysecret'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'agriculture'

mysql = MySQL(app)

def getSellingPrices():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM sellingprices')
    sellingprices = cursor.fetchall()
    return sellingprices

def getCropSellingPrices():
  return  {
        "Sunflower": 76.89,
        "Potato": 33.24,
        "Wheat": 31.32,
        "Paddy": 25.31,
        "Ragi": 38.35,
        "Barley": 35.34,
        "Maize": 30.68,
        "Carrot": 102.26,
        "Mango": 127.83,
        "Watermelon": 38.35,
        "Tomato": 76.7,
        "Banana": 34.26,
        "Cucumber": 319.57,
        "Turmeric": 102.77,
        "Sweet Potato": 35.79
    }

def saveAnalytics(userId, intake, results):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = """INSERT INTO analytics (userid, intake,results) 
                                    VALUES (%s, %s, %s)"""
    intakeJson = json.dumps(intake)
    resultsJson = json.dumps(results)
    val = (userId, intakeJson, resultsJson)
    cursor.execute(sql, val)
    mysql.connection.commit()
    return "done"

def getAnalytics(userId):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql_select_query = """select * from analytics where userId = %s"""
    # set variable in query
    cursor.execute(sql_select_query, (userId,))
    analytics = cursor.fetchall()
    return analytics

def getLatestAnalytics(userId):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql_select_query = """select results from analytics where userId = %s order by timestamp desc limit 1"""
    # set variable in query
    cursor.execute(sql_select_query, (userId,))
    latestAnalytics = cursor.fetchall()
    return latestAnalytics
