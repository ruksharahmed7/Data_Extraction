import dataExtraction.rulesfile.rules as rules
import traceback
import pandas as pd
import dataExtraction.extractionstrategy.commonfunction as commonfunction


def extract_estimated_cost_1(cluster_data,raw_cluster_data):
    try:

        json_data=[]
        cost_keyword = ''
        cost_type=''
        cost = ''
        cost_unit=''
        cost_location_track = []
        cost_flag=0
        idx=0
        back_track=0

        dict_data={}
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        df3 = pd.DataFrame()
        df4 = pd.DataFrame()
        df5 = pd.DataFrame()
        df6 = pd.DataFrame()
        df7 = pd.DataFrame()
        df8 = pd.DataFrame()
        df9 = pd.DataFrame()
        df10 = pd.DataFrame()
        df11 = pd.DataFrame()
        df12 = pd.DataFrame()
        df13 = pd.DataFrame()
        df14 = pd.DataFrame()
        df15 = pd.DataFrame()
        df16 = pd.DataFrame()
        cost_idx = 0

        result_dict={}
        for key,data in sorted(raw_cluster_data.items()):
            #print(data)
            back_track-=1
            if(back_track<=0):
                cost_flag=0
                cost_location_track.clear()
            if (not (rules.estimated_cost_re.search(data) == None) and cost_flag==0):
                mo = rules.estimated_cost_re.search(data)
                cost_keyword = mo.group(0)
                #print(cost_keyword)
                cost_location_track.append(key)
                if('(' in data and ')' in data):
                    start=data.find('(')
                    end2=data.find(')')
                    cost_unit=data[start+1:end2]
                back_track = 14
                cost_flag=1

            elif ('(' in data and ')' in data and cost_flag==1 and cost_unit==''):
                start = data.find('(')
                end2 = data.find(')')
                cost_unit = data[start + 1:end2]
                continue
            elif(not (rules.total_re.search(data) == None) and cost_flag==1):
                mo1 = rules.total_re.search(data)
                cost_type = mo1.group(0)
                #print(cost_type)
                if((':' in data or 't' in data or 'ঃ' in data) and not (rules.number_re.search(data) == None)):
                    mo2 = rules.number_re.search(data)
                    cost = mo2.group(0)
                    cost_location_track.append(key)
                    loc = commonfunction.find_location(cost_location_track)
                    dict_data = {'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit,loc],
                                                                                index=['key', 'cost_type', 'value','cost_unit',
                                                                                       'location_index'])}
                    df1 = pd.DataFrame(dict_data)
                    cost_idx += 1
                    dict_data.clear()

                    json_data.insert(idx,[cost_keyword,cost_type,cost,cost_unit])
                    json_data[idx].extend(cost_location_track)
                    idx+=1
                    cost_flag=2
                    cost_location_track.remove(key)

                    result_dict['project_cost']=cost
                    result_dict['cost_unit']=cost_unit

                else:
                    cost_flag=3
            elif (not (rules.gob_cost_re.search(data) == None) and cost_flag == 3):
                break
            elif(not (rules.number_re.search(data) == None) and cost_flag==3):
                mo=rules.number_re.search(data)
                #cost=mo.group(0)
                if (cost_unit == ''):
                    cost = data
                else:
                    cost = mo.group(0)
                cost_location_track.append(key)
                loc = commonfunction.find_location(cost_location_track)
                dict_data = {'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                          index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                 'location_index'])}
                df2 = pd.DataFrame(dict_data)
                cost_idx += 1
                dict_data.clear()
                json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                json_data[idx].extend(cost_location_track)
                idx += 1
                cost_flag=4
                cost_location_track.remove(key)
                result_dict['project_cost'] = cost
                result_dict['cost_unit'] = cost_unit
            elif (not (rules.gob_cost_re.search(data) == None) and cost_flag == 4):
                mo3 = rules.gob_cost_re.search(data)
                cost_type = mo3.group(0)
                cost_flag=5
                continue
            elif (not (rules.number_re.search(data) == None) and cost_flag == 5):
                mo = rules.number_re.search(data)
                #cost = mo.group(0)
                if (cost_unit == ''):
                    cost = data
                else:
                    cost = mo.group(0)
                cost_location_track.append(key)
                loc = commonfunction.find_location(cost_location_track)
                dict_data = {'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                          index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                 'location_index'])}
                df3 = pd.DataFrame(dict_data)
                cost_idx += 1
                dict_data.clear()

                json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                json_data[idx].extend(cost_location_track)
                idx += 1
                cost_flag = 6
                cost_location_track.remove(key)
                result_dict['gob_cost'] = cost
            elif (not (rules.not_applicable_re.search(data) == None) and cost_flag == 5):
                mo = rules.not_applicable_re.search(data)
                cost = mo.group(0)
                cost_location_track.append(key)
                loc = commonfunction.find_location(cost_location_track)
                dict_data = {'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                          index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                 'location_index'])}
                df4 = pd.DataFrame(dict_data)
                cost_idx += 1
                dict_data.clear()

                json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                json_data[idx].extend(cost_location_track)
                idx += 1
                cost_flag = 6
                cost_location_track.remove(key)
                result_dict['gob_cost'] = cost
            elif (not (rules.own_fund_re.search(data) == None) and cost_flag == 6):
                mo3 = rules.own_fund_re.search(data)
                cost_type = mo3.group(0)
                cost_flag=15
                continue
            elif (not (rules.number_re.search(data) == None) and cost_flag == 15):
                mo = rules.number_re.search(data)
                #cost = mo.group(0)
                if (cost_unit == ''):
                    cost = data
                else:
                    cost = mo.group(0)
                cost_location_track.append(key)
                loc = commonfunction.find_location(cost_location_track)
                dict_data = {'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                          index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                 'location_index'])}
                df5 = pd.DataFrame(dict_data)
                cost_idx += 1
                dict_data.clear()

                json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                json_data[idx].extend(cost_location_track)
                idx += 1
                cost_flag = 6
                cost_location_track.remove(key)
                result_dict['own_fund'] = cost
            elif (not (rules.not_applicable_re.search(data) == None) and cost_flag == 15):
                mo = rules.not_applicable_re.search(data)
                cost = mo.group(0)
                cost_location_track.append(key)
                loc = commonfunction.find_location(cost_location_track)
                dict_data = {'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                          index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                 'location_index'])}
                df6 = pd.DataFrame(dict_data)
                cost_idx += 1
                dict_data.clear()

                json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                json_data[idx].extend(cost_location_track)
                idx += 1
                cost_flag = 6
                cost_location_track.remove(key)
                result_dict['own_fund'] = cost
            elif (not (rules.pa_cost_re.search(data) == None) and cost_flag == 6):
                mo3 = rules.pa_cost_re.search(data)
                cost_type = mo3.group(0)
                cost_flag=7
                continue
            elif (not (rules.number_re.search(data) == None) and cost_flag == 7):
                mo = rules.number_re.search(data)
                #cost = mo.group(0)
                if (cost_unit == ''):
                    cost = data
                else:
                    cost = mo.group(0)
                cost_location_track.append(key)
                loc = commonfunction.find_location(cost_location_track)
                dict_data = {'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                          index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                 'location_index'])}
                df7 = pd.DataFrame(dict_data)
                cost_idx += 1
                dict_data.clear()

                json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                json_data[idx].extend(cost_location_track)
                idx += 1
                cost_flag = 8
                cost_location_track.remove(key)
                result_dict['pa_cost'] = cost
            elif (not (rules.not_applicable_re.search(data) == None) and cost_flag == 7):
                mo = rules.not_applicable_re.search(data)
                cost = mo.group(0)
                cost_location_track.append(key)
                loc = commonfunction.find_location(cost_location_track)
                dict_data = {'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                          index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                 'location_index'])}
                df8 = pd.DataFrame(dict_data)
                cost_idx += 1
                dict_data.clear()

                json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                json_data[idx].extend(cost_location_track)
                idx += 1
                cost_flag = 8
                cost_location_track.remove(key)
                result_dict['pa_cost'] = cost
            elif (not (rules.other_cost_re.search(data) == None) and cost_flag == 7):
                mo3 = rules.other_cost_re.search(data)
                cost_type = mo3.group(0)
                cost_flag = 0
                continue
            elif (not (rules.other_cost_re.search(data) == None) and cost_flag == 8):
                mo3 = rules.other_cost_re.search(data)
                cost_type = mo3.group(0)
                cost_flag=9
                continue
            elif (not (rules.number_re.search(data) == None) and cost_flag == 9):
                mo = rules.number_re.search(data)
                if(cost_unit==''):
                    cost = data
                else:
                    cost = mo.group(0)
                cost_location_track.append(key)
                loc = commonfunction.find_location(cost_location_track)
                dict_data = {'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                          index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                 'location_index'])}
                df9 = pd.DataFrame(dict_data)
                cost_idx += 1
                dict_data.clear()

                json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                json_data[idx].extend(cost_location_track)
                idx += 1
                cost_flag = 0
                cost_location_track.clear()
                result_dict['other_cost'] = cost
            elif (not (rules.not_applicable_re.search(data) == None) and cost_flag == 9):
                mo = rules.not_applicable_re.search(data)
                cost = mo.group(0)
                cost_location_track.append(key)
                loc = commonfunction.find_location(cost_location_track)
                dict_data = {'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                          index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                 'location_index'])}
                df10 = pd.DataFrame(dict_data)
                cost_idx += 1
                dict_data.clear()

                json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                json_data[idx].extend(cost_location_track)
                idx += 1
                cost_flag = 0
                cost_location_track.clear()
                result_dict['other_cost'] = cost
            elif (not (rules.gob_cost_re.search(data) == None) and cost_flag == 2):
                #print('oi kuttar baccha')
                mo3 = rules.gob_cost_re.search(data)
                cost_type = mo3.group(0)
                if ( not (rules.number_re.search(data) == None)):
                    mo4 = rules.number_re.search(data)
                    cost = mo4.group(0)
                    #print(cost)
                    #print('oi bilayer baccha')
                    cost_location_track.append(key)
                    loc = commonfunction.find_location(cost_location_track)
                    dict_data = {
                        'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                     index=['key', 'cost_type', 'value', 'cost_unit',
                                                                            'location_index'])}
                    df11 = pd.DataFrame(dict_data)
                    cost_idx += 1
                    dict_data.clear()

                    json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                    json_data[idx].extend(cost_location_track)
                    idx += 1
                    cost_flag = 10
                    cost_location_track.remove(key)
                    result_dict['gob_cost'] = cost
                    continue
                elif (not (rules.not_applicable_re.search(data) == None)):
                    mo = rules.not_applicable_re.search(data)
                    cost = mo.group(0)
                    cost_location_track.append(key)
                    loc = commonfunction.find_location(cost_location_track)
                    dict_data = {
                        'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                     index=['key', 'cost_type', 'value', 'cost_unit',
                                                                            'location_index'])}
                    df12 = pd.DataFrame(dict_data)
                    cost_idx += 1
                    dict_data.clear()

                    json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                    json_data[idx].extend(cost_location_track)
                    idx += 1
                    cost_flag = 10
                    cost_location_track.remove(key)
                    result_dict['gob_cost'] = cost
                    continue
            elif (not (rules.pa_cost_re.search(data) == None) and cost_flag == 10):
                mo5 = rules.pa_cost_re.search(data)
                cost_type = mo5.group(0)
                if (not (rules.number_re.search(data) == None)):
                    mo6 = rules.number_re.search(data)
                    cost = mo6.group(0)
                    cost_location_track.append(key)
                    loc = commonfunction.find_location(cost_location_track)
                    dict_data = {
                        'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                     index=['key', 'cost_type', 'value', 'cost_unit',
                                                                            'location_index'])}
                    df13 = pd.DataFrame(dict_data)
                    cost_idx += 1
                    dict_data.clear()

                    json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                    json_data[idx].extend(cost_location_track)
                    idx += 1
                    cost_flag = 11
                    cost_location_track.remove(key)
                    result_dict['pa_cost'] = cost
                    continue
                elif (not (rules.not_applicable_re.search(data) == None)):
                    mo = rules.not_applicable_re.search(data)
                    cost = mo.group(0)
                    cost_location_track.append(key)
                    loc = commonfunction.find_location(cost_location_track)
                    dict_data = {
                        'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                     index=['key', 'cost_type', 'value', 'cost_unit',
                                                                            'location_index'])}
                    df14 = pd.DataFrame(dict_data)
                    cost_idx += 1
                    dict_data.clear()

                    json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                    json_data[idx].extend(cost_location_track)
                    idx += 1
                    cost_flag = 11
                    cost_location_track.remove(key)
                    result_dict['pa_cost'] = cost
                    continue
                elif (not (rules.other_cost_re.search(data) == None) and cost_flag == 11):
                    mo5 = rules.other_cost_re.search(data)
                    cost_type = mo5.group(0)
                    if (not (rules.not_applicable_re.search(data) == None)):
                        mo = rules.not_applicable_re.search(data)
                        cost = mo.group(0)
                        cost_location_track.append(key)
                        loc = commonfunction.find_location(cost_location_track)
                        dict_data = {
                            'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                         index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                'location_index'])}
                        df15 = pd.DataFrame(dict_data)
                        cost_idx += 1
                        dict_data.clear()

                        json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                        json_data[idx].extend(cost_location_track)
                        idx += 1
                        cost_flag = 0
                        cost_location_track.clear()
                        result_dict['other_cost'] = cost

                    elif (not (rules.number_re.search(data) == None)):
                        mo6 = rules.number_re.search(data)
                        cost = mo6.group(0)
                        cost_location_track.append(key)
                        loc = commonfunction.find_location(cost_location_track)
                        dict_data = {
                            'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, cost_type, cost, cost_unit, loc],
                                                                         index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                'location_index'])}
                        df16 = pd.DataFrame(dict_data)
                        cost_idx += 1
                        dict_data.clear()

                        json_data.insert(idx, [cost_keyword, cost_type, cost, cost_unit])
                        json_data[idx].extend(cost_location_track)
                        idx += 1
                        cost_flag = 0
                        cost_location_track.clear()
                        result_dict['other_cost'] = cost
        result_df = pd.concat([df1, df2, df3, df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16], axis=1, sort=False)
        #print(result)
        del df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16
        return json_data,result_df,result_dict
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())


def extract_estimated_cost_2(cluster_data,raw_cluster_data):
    try:
        json_data=[]
        cost_keyword = ''
        cost_type=[]
        cost = ''
        total_cost=''
        gob_cost=''
        own_cost=''
        pa_cost=''
        other_cost=''
        cost_unit=''
        cost_location_track = []
        cost_flag=0
        idx=0
        back_track=0
        result_dict={}
        dict_data = {}
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        df3 = pd.DataFrame()
        cost_idx=0
        list_idx=0
        cost_type_flag=[]
        for key,data in sorted(raw_cluster_data.items()):
            #print(data)
            back_track-=1
            if(back_track<=0):
                cost_flag=0
                cost_location_track.clear()
            if (not (rules.estimated_cost_re.search(data) == None) and cost_flag==0):
                mo = rules.estimated_cost_re.search(data)
                cost_keyword = mo.group(0)
                #print(cost_keyword
                cost_location_track.append(key)
                if ('(' in data and ')' in data):
                    start = data.find('(')
                    end2 = data.find(')')
                    cost_unit = data[start + 1:end2]
                    #print(cost_unit)
                cost_flag = 1
                back_track = 12
            if ('(' in data and ')' in data and cost_flag == 1 and cost_unit == ''):
                start = data.find('(')
                end2 = data.find(')')
                cost_unit = data[start + 1:end2]
                #print('Here:'+cost_unit)
                if (not (rules.total_re.search(data) == None) and cost_flag == 1):
                    #print("sdfsdgdfs")
                    mo1 = rules.total_re.search(data)
                    cost_type.insert(list_idx, mo1.group(0))
                    list_idx += 1
                    total_cost_key = mo1.group(0)
                    #print(total_cost_key)
                    back_track = 8
                    cost_type_flag.append(1)
            elif (not (rules.total_re.search(data) == None) and cost_flag == 1):
                #print("sdfsdgdfs")
                mo1 = rules.total_re.search(data)
                cost_type.insert(list_idx,mo1.group(0))
                list_idx+=1
                total_cost_key=mo1.group(0)
                #print(total_cost_key)
                back_track = 8
                cost_type_flag.append(1)
            elif (not (rules.gob_cost_re.search(data) == None) and cost_flag == 1):
                #print("fd")
                mo1 = rules.gob_cost_re.search(data)
                cost_type.insert(list_idx,mo1.group(0))
                list_idx+=1
                gob_cost=mo1.group(0)
                cost_type_flag.append(2)
            elif (not (rules.own_fund_re.search(data) == None) and cost_flag == 1):
                mo1 = rules.own_fund_re.search(data)
                cost_type.insert(list_idx,mo1.group(0))
                list_idx+=1
                own_cost=mo1.group(0)
                cost_type_flag.append(3)
            elif (not (rules.pa_cost_re.search(data) == None) and cost_flag == 1):
                mo1 = rules.pa_cost_re.search(data)
                cost_type.insert(list_idx,mo1.group(0))
                list_idx+=1
                pa_cost=mo1.group(0)
                cost_type_flag.append(4)
            elif (not (rules.other_cost_re.search(data) == None) and cost_flag == 1):
                mo1 = rules.other_cost_re.search(data)
                cost_type.insert(list_idx,mo1.group(0))
                other_cost=mo1.group(0)
                cost_type_flag.append(5)
            elif (not (rules.number_re.search(data) == None) and cost_flag == 1):
                if 1 in cost_type_flag[:]:
                    mo = rules.number_re.search(data)
                    cost = mo.group(0)
                    total_cost=cost
                    cost_location_track.append(key)

                    loc = commonfunction.find_location(cost_location_track)
                    dict_data = {
                        'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, total_cost, cost, cost_unit, loc],
                                                                     index=['key', 'cost_type', 'value', 'cost_unit',
                                                                            'location_index'])}
                    df1 = pd.DataFrame(dict_data)
                    cost_idx += 1
                    dict_data.clear()

                    json_data.insert(idx, [cost_keyword, total_cost, cost, cost_unit])
                    json_data[idx].extend(cost_location_track)
                    idx += 1
                    cost_flag = 2
                    cost_location_track.remove(key)
                    result_dict['cost_unit'] = cost_unit
                    result_dict['project_cost'] = cost
            elif (not (rules.number_re.search(data) == None) and cost_flag == 2):
                if 2 in cost_type_flag[:]:
                    mo = rules.number_re.search(data)
                    cost = mo.group(0)
                    gob_cost=cost
                    cost_location_track.append(key)
                    loc = commonfunction.find_location(cost_location_track)
                    dict_data = {'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, gob_cost, cost, cost_unit, loc],
                                                                     index=['key', 'cost_type', 'value', 'cost_unit',
                                                                            'location_index'])}
                    df2 = pd.DataFrame(dict_data)
                    cost_idx += 1
                    dict_data.clear()
                    json_data.insert(idx, [cost_keyword, gob_cost, cost, cost_unit])
                    json_data[idx].extend(cost_location_track)
                    idx += 1
                    cost_flag = 3
                    cost_location_track.remove(key)
                    result_dict['gob_cost'] = cost
            elif (not (rules.number_re.search(data) == None) and cost_flag == 3):
                if 3 in cost_type_flag[:]:
                    mo = rules.number_re.search(data)
                    cost = mo.group(0)
                    cost_location_track.append(key)
                    if(total_cost!=gob_cost):
                        loc = commonfunction.find_location(cost_location_track)
                        dict_data = {
                            'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, own_cost, cost, cost_unit, loc],
                                                                         index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                'location_index'])}
                        df3 = pd.DataFrame(dict_data)
                        cost_idx += 1
                        dict_data.clear()
                        json_data.insert(idx, [cost_keyword, own_cost, cost, cost_unit])
                        json_data[idx].extend(cost_location_track)
                        idx += 1
                    cost_flag = 4
                    cost_location_track.remove(key)
                    result_dict['own_fund'] = cost
            elif (not (rules.number_re.search(data) == None) and cost_flag == 3 and pa_cost!=''):
                if 4 in cost_type_flag[:]:
                    mo = rules.number_re.search(data)
                    cost = mo.group(0)
                    cost_location_track.append(key)
                    if(total_cost!=gob_cost):
                        loc = commonfunction.find_location(cost_location_track)
                        dict_data = {
                            'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, pa_cost, cost, cost_unit, loc],
                                                                         index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                'location_index'])}
                        df3 = pd.DataFrame(dict_data)
                        cost_idx += 1
                        dict_data.clear()
                        json_data.insert(idx, [cost_keyword, pa_cost, cost, cost_unit])
                        json_data[idx].extend(cost_location_track)
                        idx += 1
                    cost_flag = 4
                    cost_location_track.remove(key)
                    result_dict['pa_cost'] = cost
            elif (not (rules.number_re.search(data) == None) and cost_flag == 4 and other_cost!=''):
                if 5 in cost_type_flag[:]:
                    mo = rules.number_re.search(data)
                    cost = mo.group(0)
                    cost_location_track.append(key)
                    if(total_cost!=gob_cost):
                        loc = commonfunction.find_location(cost_location_track)
                        dict_data = {
                            'Estimated_cost_' + str(cost_idx): pd.Series([cost_keyword, other_cost, cost, cost_unit, loc],
                                                                         index=['key', 'cost_type', 'value', 'cost_unit',
                                                                                'location_index'])}
                        df3 = pd.DataFrame(dict_data)
                        cost_idx += 1
                        dict_data.clear()
                        json_data.insert(idx, [cost_keyword, other_cost, cost, cost_unit])
                        json_data[idx].extend(cost_location_track)
                        idx += 1
                    cost_flag = 0
                    cost_location_track.remove(key)
                    result_dict['other_cost'] = cost
        print(cost_type_flag)
        result_df = pd.concat([df1, df2, df3], axis=1, sort=False)
        del df1,df2,df3
        return json_data,result_df,result_dict
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None,None,None
