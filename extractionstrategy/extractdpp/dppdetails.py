from pprint import pprint

import dataExtraction.rulesfile.rules as rules
import dataExtraction.tracking.trackingprojectid as tracking
import re
import time
leter=re.compile(r'[a-zA-Z]')

def extract_all(raw_cluser_data,cleaned_cluster_data,project_id):
    print('ALl Extraction')
    result_dict={}
    result_list=[]
    project_name=''
    project_name_key=[]
    total_cost=''
    gob_cost=''
    pa_cost=''
    own_fund=''
    other_cost=''
    revised_total_cost = ''
    revised_gob_cost = ''
    revised_pa_cost = ''
    revised_other_cost = ''
    cost_unit=''
    cost_key=[]
    start_date=''
    revised_start_date=''
    start_date_key=0
    end_date=''
    revised_end_date=''
    end_date_key=0
    date_key=[]
    ministry=''
    ministry_key=0
    executing_agency=''
    executing_agency_key=0
    planning_division=''
    planning_division_key=0
    flag=0
    cost_track=0
    back_track=0
    flag_unit=0
    pprint(raw_cluser_data)
    for key,value in sorted(raw_cluser_data.items()):
        print(key,value)
        if(not (rules.project_name_re.search(value)==None) and flag==0 and ':' in value):
            idx=value.find(':')
            project_name=value[idx+1:]
            #print('herr')
            project_name_key.append(key)
            flag=10
            continue
        elif(not (rules.project_name_re.search(value)==None) and flag==0 and ':' not in value):
            flag=1
            continue
        elif(flag==1 and rules.point_re.search(value)==None):
            project_name+=' '+value
            project_name_key.append(key)
        elif(not rules.point_re.search(value)==None and flag==1):
            flag=0
        elif(flag==0 and not (rules.ministy_re.search(value)==None)):
            flag=2
        elif(flag==2 and rules.point_re.search(value)==None):
            ministry=value
            ministry_key=key
        elif (not rules.point_re.search(value) == None and flag == 2):
            flag = 0
        elif (flag == 0 and not (rules.agency_re.search(value) == None)):
            flag = 3
        elif (flag == 3 and rules.point_re.search(value) == None):
            executing_agency = value
            executing_agency_key = key
        elif (not rules.point_re.search(value) == None and flag == 3):
            flag = 0
        elif (flag == 0 and not (rules.planning_re.search(value) == None)):
            flag = 4
        elif (flag == 4 and rules.point_re.search(value) == None):
            planning_division = value
            planning_division_key = key
        elif (not rules.point_re.search(value) == None and flag == 4):
            flag = 0
        elif(not rules.date_re.search(value)==None and flag==0):
            flag=5
        elif(flag==5 and not rules.original_date_re.search(value)==None):
            flag=25
            continue
        elif(flag==25):
            start_date=value
            date_key.append(key)
            flag=6
            continue
        elif(flag==6):
            end_date=value
            date_key.append(key)
            flag=0
        elif(flag==0 and not rules.revised_date_re.search(value)==None):
            flag=7
            continue
        elif (flag == 7):
            revised_start_date = value
            date_key.append(key)
            flag = 8
            continue
        elif (flag == 8):
            revised_end_date = value
            date_key.append(key)
            flag = 0
        elif(flag==0 and not rules.estimated_cost_re.search(value)==None):
            if('(' in value):
                idx1=value.find('(')
                idx2=value.find(')')
                cost_unit=value[idx1+1:idx2]
            else:
                flag_unit=1
            flag=30
        if(flag_unit==1 and 'Taka' in value):
            idx1 = value.find('(')
            idx2 = value.find(')')
            cost_unit = value[idx1 + 1:idx2]
            flag_unit=0
        elif(flag==30 and not rules.original_cost_re.search(value)==None ):
            cost_track=1
        elif (flag == 30 and not rules.revised_cost_re.search(value) == None):
            cost_track = 2
        elif(flag==30 and cost_track==2 and not rules.total_re.search(value)==None):
            flag=31
            continue
        elif(flag==31):
            total_cost=value
            flag=32
        elif(flag==32):
            revised_total_cost=value
            flag=33
        elif(flag==33 and not rules.gob_cost_re.search(value)==None):
            flag=34
            continue
        elif(flag==34):
            gob_cost=value
            flag=35
        elif(flag==35):
            revised_gob_cost=value
            flag=36
        elif(flag==36 and not rules.pa_cost_re.search(value)==None):
            flag=37
            continue
        elif(flag == 37 and rules.amount_re.search(value) == None):
            flag=39
        elif (flag == 37):
            pa_cost = value
            flag = 38
        elif (flag == 38):
            revised_pa_cost = value
            flag = 39
        elif (flag == 39 and not rules.other_cost_re.search(value) == None):
            flag = 40
            back_track=1
            continue
        elif(flag == 40 and rules.amount_re.search(value) == None and back_track > 0):
            back_track-=1
            flag=0
        elif (flag == 40):
            other_cost = value
            flag = 41
        elif (flag == 41):
            revised_other_cost = value
            flag = 0


        elif(flag==10 and rules.ministy_re.search(value)==None):
            #print(project_name)
            project_name+=' '+value
            project_name_key.append(key)
        elif (flag == 10 and not (rules.ministy_re.search(value) == None)):
            #print('ministry')
            idx = value.find(':')
            ministry = value[idx + 1:]
            ministry_key=key
            flag = 11
        elif (flag == 11 and not (rules.agency_re.search(value) == None)):
            idx = value.find(':')
            executing_agency = value[idx + 1:]
            executing_agency_key=key
            flag = 12
        elif (flag == 12 and not (rules.planning_re.search(value) == None)):
            idx = value.find(':')
            planning_division= value[idx + 1:]
            planning_division_key=key
            flag = 13
        elif((flag==13 or flag==12)  and not (rules.start_date_re.search(value)==None)):
            idx = value.find(':')
            start_date = value[idx + 1:]
            start_date_key = key
            flag = 14
        elif (flag == 14 and not (rules.end_date_re.search(value) == None)):
            idx = value.find(':')
            end_date = value[idx + 1:]
            end_date_key = key
            flag = 15
        elif (flag == 15 and not (rules.estimated_cost_re.search(value) == None)):
            idx1 = value.find('(')
            idx2=value.find(')')
            cost_unit= value[idx1+ 1:idx2]
            cost_key.append(key)
            flag = 16
        elif (flag == 16 and not (rules.total_re.search(value) == None)):
            idx = value.find(':')
            total_cost = value[idx + 1:]
            cost_key.append(key)
        elif (flag == 16 and not (rules.gob_cost_re.search(value) == None)):
            idx = value.find(':')
            gob_cost = value[idx + 1:]
            cost_key.append(key)
        elif (flag == 16 and not (rules.pa_cost_re.search(value) == None)):
            idx = value.find(':')
            pa_cost = value[idx + 1:]
            cost_key.append(key)
        elif (flag == 16 and not (rules.own_fund_re.search(value) == None)):
            idx = value.find(':')
            own_fund = value[idx + 1:]
            cost_key.append(key)
        elif (flag == 16 and not (rules.other_cost_re.search(value) == None)):
            idx = value.find(':')
            other_cost = value[idx + 1:]
            cost_key.append(key)
            flag = 20

    #print(project_name,ministry,executing_agency,planning_division,start_date,end_date,cost_unit,total_cost,gob_cost,pa_cost,other_cost)
    #print(start_date,end_date,revised_start_date,revised_end_date)
    #print(total_cost,revised_total_cost,gob_cost,revised_gob_cost,pa_cost,revised_pa_cost,other_cost,revised_other_cost)
    mo=leter.search(project_name)
    project_name_eng=''
    project_name_ban=''
    if(not mo==None):
        ltr=mo.group(0)
        idx=project_name.find(ltr)
        project_name_ban=project_name[:idx]
        project_name_eng=project_name[idx:]
    else:
        project_name_ban=project_name
    result_dict={
        'approval_date':'',
        'project_id':project_id,
        'project_name':project_name_ban,
        'project_name_english':project_name_eng,
        'project_cost':total_cost,
        'cost_unit':cost_unit,
        'gob_cost':gob_cost,
        'own_fund':own_fund,
        'pa_cost':pa_cost,
        'other_cost':other_cost,
        'revised_project_cost':revised_total_cost,
        'revised_gob_cost':revised_gob_cost,
        'revised_pa_cost':revised_pa_cost,
        'revised_other_cost':revised_other_cost,
        'start_date':start_date,
        'end_date':end_date,
        'revised_start_date':revised_start_date,
        'revised_end_date':revised_end_date,
        'sponsoring_ministry':ministry,
        'executing_agency':executing_agency,
        'planning_division':planning_division,
    }
    #p_id = tracking.get_project_id(project_name_ban)
    #if str(p_id) == str(project_id):
     #   result_list.append(result_dict)
    result_list.append(result_dict)
    return result_list
