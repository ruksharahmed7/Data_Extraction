import dataExtraction.rulesfile.rules as rules
import traceback
import pandas as pd
import dataExtraction.extractionstrategy.commonfunction as commonfunction
import dataExtraction.clustering.clusteringdpp as clusteringdpp

def extract_organization1(operational_data):
    try:
        operational_cluster_data=clusteringdpp.find_projectorg_data(operational_data)
        json_data = []
        dict_data = {}
        result_dict={}
        sponsoring_ministry_key = ''
        sponsoring_ministry=''
        executing_agency_key=''
        executing_agency=''
        planning_division_key=''
        planning_division=''
        location_track=0
        location_track_list = []
        org_flag = 0
        idx = 0
        idx1=0
        idx2=0
        idx3=0
        back_track = 0
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        df3 = pd.DataFrame()
        for key,data in sorted(operational_cluster_data.items()):
            #print(key,data)
            back_track -= 1
            if (back_track <= 0):
                date_flag = 0
            if (not (rules.ministy_re.search(data) == None) and org_flag==0):
                mo = rules.ministy_re.search(data)
                sponsoring_ministry_key = mo.group(0)
                #print(sponsoring_ministry_key)
                location_track_list.append(key)
                org_flag=1
                back_track=8
            elif(rules.point_re.search(data)==None and org_flag==1):
                sponsoring_ministry=data
                location_track_list.append(key)
                org_flag=2
            elif (not (rules.agency_re.search(data) == None) and org_flag==2):
                mo = rules.agency_re.search(data)
                executing_agency_key = mo.group(0)
                #print(executing_agency_key)
                location_track_list.append(key)
                org_flag=3
            elif(rules.point_re.search(data)==None and org_flag==3):
                executing_agency=data
                location_track_list.append(key)
                org_flag=5
            elif (not (rules.planning_re.search(data) == None) and org_flag==5):
                mo = rules.planning_re.search(data)
                planning_division_key = mo.group(0)
                #print(planning_division_key)
                location_track_list.append(key)
                org_flag=6
            elif(rules.point_re.search(data)==None and org_flag==6):
                planning_division=data
                loc1=location_track_list[0]
                loc2 = location_track_list[1]
                dict_data = {'sponsoring_ministry_' + str(idx1): pd.Series(
                    [sponsoring_ministry_key, sponsoring_ministry, str(loc1) + ',' + str(loc2)],
                    index=['key', 'value',
                           'location_index'])}
                df1 = pd.DataFrame(dict_data)
                idx1 += 1
                result_dict['sponsoring_ministry']=sponsoring_ministry


                loc1=location_track_list[2]
                loc2=location_track_list[3]
                dict_data = {'executing_agency_' + str(idx2): pd.Series(
                    [executing_agency_key, executing_agency, str(loc1) + ',' + str(loc2)],
                    index=['key', 'value',
                           'location_index'])}
                df2 = pd.DataFrame(dict_data)
                idx2 += 1
                dict_data.clear()
                result_dict['executing_agency']=executing_agency

                loc=location_track_list[4]
                dict_data = {'planning_division_' + str(idx3): pd.Series([planning_division_key, planning_division,  str(loc)+','+str(key)],
                                                                            index=['key', 'value',
                                                                                   'location_index'])}
                df3 = pd.DataFrame(dict_data)
                idx3 += 1
                dict_data.clear()
                result_dict['planning_division']=planning_division
                location_track_list.clear()
                org_flag=0
        result_df = pd.concat([df1, df2, df3], axis=1, sort=False)
        #print(result)
        del df1, df2, df3
        return result_df,result_dict
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None,None

def extract_organization_3(operational_data):
    data_dict={}
    flag=0
    for key,value in sorted(operational_data.items()):
        #print(value)
        if(not rules.ministy_re.search(value)==None and flag==0):
            flag=1
            #print('found')
            continue
        elif(rules.trackorg_re.match(value)):
            break
        elif(flag==1 and rules.agency_re.search(value)==None):
            data_dict['sponsoring_ministry']=value
            #print(data_dict)
            flag=0
        elif(not rules.agency_re.search(value)==None and flag==0):
            flag=2
            continue
        elif(flag==2 and rules.planning_re.search(value)==None):
            data_dict['executing_agency']=value
            flag=0
        elif(not rules.planning_re.search(value)==None and flag==0):
            flag=3
            continue
        elif(flag==3 and not rules.trackorg_re.search(value)):
            data_dict['planning_division']=value
            break

    return data_dict



def extract_organization_2(operational_data):
    try:
        operational_cluster_data = clusteringdpp.find_projectorg_data(operational_data)
        print(operational_cluster_data)
        dict_data = {}
        result_dict={}
        sponsoring_ministry_key = 0
        sponsoring_ministry_key_data = ''
        sponsoring_ministry = ''
        partner_ministry_key=0
        partner_ministry=''
        executing_agency_key = 0
        executing_agency_key_data = ''
        executing_agency = ''
        sector_key_data = ''
        sector = ''
        partner_agency_key=0
        partner_agency=''
        planning_division_key = 0
        planning_division_key_data = ''
        planning_division = ''
        location_track = 0
        location_track_list = []
        ministry_key=[]
        partnermin_key=[]
        agency_key=[]
        partneragen_key=[]
        planning_key=[]
        org_flag = 0
        idx = 0
        idx1 = 0
        idx2 = 0
        idx3 = 0
        back_track = 0
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        df3 = pd.DataFrame()
        df4 = pd.DataFrame()
        df5 = pd.DataFrame()
        for key, data in sorted(operational_cluster_data.items()):
            print(data)
            if (not (rules.ministy_re.search(data) == None) and org_flag==0):
                sponsoring_ministry_key = key
                print(data)
                #print(sponsoring_ministry_key)
                #location_track_list.append(key)
                if(':' in data or '\t' in data or 'ঃ' in data):
                    print(data)
                    org_flag = 10
                    track = commonfunction.find_index(data)
                    sponsoring_ministry_key_data = data[:track]
                    sponsoring_ministry = data[track + 1:]
                    dict_data = {'sponsoring_ministry': pd.Series(
                        [sponsoring_ministry_key_data, sponsoring_ministry,
                         str(key)],
                        index=['key', 'value',
                               'location_index'])}
                    df1 = pd.DataFrame(dict_data)
                    dict_data.clear()
                    result_dict['sponsoring_ministry']=sponsoring_ministry
                    continue
                org_flag=1
                continue
            elif(not (rules.stop_org_re.search(data)==None)):
                break
            elif (not (rules.partner_ministry_re.search(data) == None) and org_flag == 1):
                org_flag = 4
                partner_ministry_key = key
            if (not(rules.partner_agency_re.search(data)==None) and org_flag!=10):
                org_flag = 5
                partner_agency_key = key
                continue
            elif (org_flag == 4 and rules.agency_re.search(data) == None):
                partnermin_key.append(key)
            elif(org_flag==1 and rules.agency_re.search(data)==None):
                ministry_key.append(key)
            elif(not(rules.agency_re.search(data)==None) and org_flag!=10):
                org_flag=2
                executing_agency_key=key
                continue
                #print('here:',clustered_data[key])
            elif (org_flag == 5):
                partneragen_key.append(key)
            elif(org_flag==2 and rules.planning_re.search(data)==None):
                agency_key.append(key)
            elif(not (rules.planning_re.search(data)==None) and org_flag!=10):
                org_flag=3
                planning_division_key=key
                continue
            elif(org_flag==3):
                planning_key.append(key)

            elif (not (rules.agency_re.search(data) == None) and org_flag == 10):
                track = commonfunction.find_index(data)
                executing_agency_key_data = data[:track]
                executing_agency = data[track + 1:]
                dict_data = {'executing_agency': pd.Series(
                    [executing_agency_key_data, executing_agency,
                     str(key)],
                    index=['key', 'value',
                           'location_index'])}
                df2 = pd.DataFrame(dict_data)
                dict_data.clear()
                result_dict['executing_agency']=executing_agency

            elif (not (rules.sector_re.search(data) == None) and org_flag == 10):
                track = commonfunction.find_index(data)
                sector_key_data = data[:track]
                sector = data[track + 1:]
                dict_data = {'sector': pd.Series(
                    [sector_key_data, sector,
                     str(key)],
                    index=['key', 'value',
                           'location_index'])}
                df3 = pd.DataFrame(dict_data)
                dict_data.clear()
                result_dict['sector']=sector
                continue
            elif (not (rules.planning_re.search(data) == None) and org_flag == 10):
                track = commonfunction.find_index(data)
                planning_division_key_data = data[:track]
                planning_division = data[track + 1:]
                dict_data = {'planning_division': pd.Series(
                    [planning_division_key_data, planning_division,
                     str(key)],
                    index=['key', 'value',
                           'location_index'])}
                df4 = pd.DataFrame(dict_data)
                dict_data.clear()
                result_dict['planning_division']=planning_division


        if(sponsoring_ministry_key!=0 and len(ministry_key)>0):
            for k in ministry_key:
                sponsoring_ministry+=operational_data[k]
                location_track_list.append(k)
            loc = commonfunction.find_location(location_track_list)
            dict_data = {'sponsoring_ministry': pd.Series(
                [operational_data[sponsoring_ministry_key], sponsoring_ministry, str(sponsoring_ministry_key) + ',' + loc],
                index=['key', 'value',
                       'location_index'])}
            df1 = pd.DataFrame(dict_data)
            idx1 += 1
            dict_data.clear()
            location_track_list.clear()
            result_dict['sponsoring_ministry']=sponsoring_ministry

        if (partner_ministry_key != 0 and len(partnermin_key) > 0):
            for k in partnermin_key:
                partner_ministry += operational_data[k]
                location_track_list.append(k)
            loc = commonfunction.find_location(location_track_list)
            dict_data = {'partner_ministry': pd.Series(
                [operational_data[partner_ministry_key], partner_ministry,
                 str(partner_ministry_key) + ',' + loc],
                index=['key', 'value',
                       'location_index'])}
            df2 = pd.DataFrame(dict_data)
            idx1 += 1
            dict_data.clear()
            location_track_list.clear()
            result_dict['partner_ministry']=partner_ministry

        if (executing_agency_key != 0 and len(agency_key) > 0):
            for k in agency_key:
                executing_agency += operational_data[k]
                location_track_list.append(k)
            loc = commonfunction.find_location(location_track_list)
            dict_data = {'executing_agency': pd.Series(
                [operational_data[executing_agency_key], executing_agency,
                 str(executing_agency_key) + ',' + loc],
                index=['key', 'value',
                       'location_index'])}
            df3 = pd.DataFrame(dict_data)
            idx1 += 1
            dict_data.clear()
            location_track_list.clear()
            result_dict['executing_agency']=executing_agency

        if (partner_agency_key != 0 and len(partneragen_key) > 0):
            for k in partneragen_key:
                partner_agency += operational_data[k]
                location_track_list.append(k)
            loc = commonfunction.find_location(location_track_list)
            dict_data = {'partner_executing_agency': pd.Series(
                [operational_data[partner_agency_key], partner_agency,
                 str(partner_agency_key) + ',' + loc],
                index=['key', 'value',
                       'location_index'])}
            df4 = pd.DataFrame(dict_data)
            idx1 += 1
            dict_data.clear()
            location_track_list.clear()
            result_dict['partner_executing_agency']=partner_agency
        if (planning_division_key != 0 and len(planning_key) > 0):
            for k in planning_key:
                planning_division += operational_data[k]
                location_track_list.append(k)
            loc = commonfunction.find_location(location_track_list)
            dict_data = {'planning_division': pd.Series(
                [operational_data[planning_division_key], planning_division,
                 str(planning_division_key) + ',' + loc],
                index=['key', 'value',
                       'location_index'])}
            df5 = pd.DataFrame(dict_data)
            idx1 += 1
            dict_data.clear()
            location_track_list.clear()
            result_dict['planning_division']=planning_division

        result_df = pd.concat([df1, df2, df3,df4,df5], axis=1, sort=False)
        #print(result)
        del df1, df2, df3, df4, df5
        return result_df,result_dict

    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None,None
"""
def extract_org_data_2(clustered_data):
    org_flag=0
    data=''
    key=0
    org_flag = 10
    track = commonfunction.find_index(data)
    sponsoring_ministry_key_data = data[:track]
    sponsoring_ministry = data[track + 1:]
    dict_data = {'sponsoring_ministry': pd.Series(
        [sponsoring_ministry_key_data, sponsoring_ministry,
         str(key)],
        index=['key', 'value',
               'location_index'])}
    df1 = pd.DataFrame(dict_data)
    dict_data.clear()
    elif (not (rules.agency_re.search(data) == None) and org_flag == 10):
    track = commonfunction.find_index(data)
    executing_agency_key_data = data[:track]
    executing_agency = data[track + 1:]
    dict_data = {'executing_agency': pd.Series(
        [executing_agency_key_data, executing_agency,
         str(key)],
        index=['key', 'value',
               'location_index'])}
    df2 = pd.DataFrame(dict_data)
    dict_data.clear()

elif (not (rules.sector_re.search(data) == None) and org_flag == 10):
track = commonfunction.find_index(data)
sector_key_data = data[:track]
sector = data[track + 1:]
dict_data = {'sector': pd.Series(
    [sector_key_data, sector,
     str(key)],
    index=['key', 'value',
           'location_index'])}
df3 = pd.DataFrame(dict_data)
dict_data.clear()
continue
elif (not (rules.planning_re.search(data) == None) and org_flag == 10):
track = commonfunction.find_index(data)
planning_division_key_data = data[:track]
planning_division = data[track + 1:]
dict_data = {'planning_division': pd.Series(
    [planning_division_key_data, planning_division,
     str(key)],
    index=['key', 'value',
           'location_index'])}
df4 = pd.DataFrame(dict_data)
dict_data.clear()
"""

