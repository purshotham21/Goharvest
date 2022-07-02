from service import farmingRepository

def calculateAllocations(name,weather,crops):
    print('Calculating allocations for crops:',crops,', under weather:',weather)
    allocations = {'farmer': name, 'weather':weather, 'allocations': {'potato':30, 'tomato':40, 'apple':30}}
    runModel()
    return allocations


def runModel(Dict):
    crop1 = Dict.get('crops')[0]
    crop2 = Dict.get('crops')[1]
    crop3 = Dict.get('crops')[2]
    print(crop1)
    print(crop2)
    print(crop3)
    pct_sc1 =Dict.get('pct_sc1')
    pct_sc2 =Dict.get('pct_sc2')
    pct_sc3 =Dict.get('pct_sc3')

    total_space =Dict.get('total_space')

    revenue_crop1 = Dict.get('revenue_crop1')
    revenue_crop2 = Dict.get('revenue_crop2')
    revenue_crop3 = Dict.get('revenue_crop3')

    sc1_crop1 = Dict.get('sc1_crop1')
    sc1_crop2 = Dict.get('sc1_crop2')
    sc1_crop3 = Dict.get('sc1_crop3')

    sc2_crop1 = Dict.get('sc2_crop1')
    sc2_crop2 = Dict.get('sc2_crop2')
    sc2_crop3 = Dict.get('sc2_crop3')

    sc3_crop1 = Dict.get('sc3_crop1')
    sc3_crop2 = Dict.get('sc3_crop2')
    sc3_crop3 = Dict.get('sc3_crop3')

    #for Scenerio 1
    for a1 in range(0,sc1_crop1+1):
        #print('hello\n')
        for b1 in range(0,sc1_crop2+1):
            #print('there\n')
            for c1 in range(0,sc1_crop3+1):
                #print(a + b + c, end=' ')
                temp_total_sc1 = a1 + b1 + c1
                if(temp_total_sc1 <= total_space):
                    sc1_total = pct_sc1* (a1*revenue_crop1 + b1*revenue_crop2 + c1 *revenue_crop3)
                    swap_a1=a1
                    swap_b1=b1
                    swap_c1=c1
                else:
                    x=0;
    #for Scenerio 2
    for a2 in range(0,sc2_crop1+1):
        #print('hello\n')
        for b2 in range(0,sc2_crop2+1):
            #print('there\n')
            for c2 in range(0,sc2_crop3+1):
                #print(a + b + c, end=' ')
                temp_total_sc2 = a2 + b2 + c2
                if(temp_total_sc2 <= total_space):
                    sc2_total = pct_sc2* (a2*revenue_crop1 + b2*revenue_crop2 + c2 *revenue_crop3)
                    swap_a2=a2
                    swap_b2=b2
                    swap_c2=c2
                else:
                    x=0;
    #for Scenerio 3
    for a3 in range(0,sc3_crop1+1):
        #print('hello\n')
        for b3 in range(0,sc3_crop2+1):
            #print('there\n')
            for c3 in range(0,sc3_crop3+1):
                #print(a + b + c, end=' ')
                temp_total_sc3 = a3 + b3 + c3
                if(temp_total_sc3 <= total_space):
                    sc3_total = pct_sc3* (a3*revenue_crop1 + b3*revenue_crop2 + c3 *revenue_crop3)
                    swap_a3 = a3
                    swap_b3 = b3
                    swap_c3 = c3
                    xxx='copydone'
                else:
                    x=0;


    print(xxx)
    final_total_revenue = sc1_total + sc2_total + sc3_total
    final_total_revenue
    if (sc1_total >= sc2_total) and (sc1_total >= sc3_total):
        largest = sc1_total
        scn= 'Scenerio 1'
        pct_final= pct_sc1
        value_crop1=swap_a1
        value_crop2=swap_b1
        value_crop3=swap_c1
    elif (sc2_total >= sc1_total) and (sc2_total >= sc3_total):
        largest = sc2_total
        scn = 'Scenerio 2'
        pct_final= pct_sc2
        value_crop1=swap_a2
        value_crop2=swap_b2
        value_crop3=swap_c2
    else:
        largest = sc3_total
        scn = 'Scenerio 3'
        pct_final= pct_sc3
        value_crop1=swap_a3
        value_crop2=swap_b3
        value_crop3=swap_c3
    print("The largest number and Scenerio is", largest, scn)
    print('Value taken for Crop is a,b,c : ', value_crop1,value_crop2,value_crop3)
    crop_allocation1 = ((pct_final *(value_crop1 * revenue_crop1)) / (largest)) * 100
    crop_allocation2 = ((pct_final *(value_crop2 * revenue_crop2)) / (largest)) * 100
    crop_allocation3 = ((pct_final *(value_crop3 * revenue_crop3)) / (largest)) * 100
    print(crop_allocation1)
    print(crop_allocation2)
    print(crop_allocation3)
    final_total_revenue
    results = {
        "profit":round(final_total_revenue,2),
        "allocations":[{
            "crop": crop1,
            "allocation":round(crop_allocation1,2)
        },{
            "crop":crop2,
            "allocation":round(crop_allocation2,2)
        },{
            "crop":crop3,
            "allocation":round(crop_allocation3,2)
        }]
    }
    return results