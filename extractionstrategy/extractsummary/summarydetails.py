import dataExtraction.rulesfile.summaryrules as rules
import dataExtraction.datapreprocessing.processingdata as getcleandata
import pandas as pd
import traceback
import time
from pprint import pprint
import dataExtraction.tracking.trackingprojectid as tracking

def summary_extract(clustered_data,raw_data):
    result_list=[]
    dict_data={}
    project_id=''
    approval_date=''
    approval_date_key=''
    division=''
    division_key=''
    df1 = pd.DataFrame()
    result=pd.DataFrame()
    project_track_dict={}
    flag=0
    confidence_level=0
    project_name_save=''
    #pprint(clustered_data)
    for key, values in sorted(clustered_data.items()):
        #print(values)
        if (flag == 1):

            print(values)
            confidence_level=1
            project_name,total_cost,start_date,end_date=extract_other(values)
            print(project_name,total_cost,start_date,end_date)
            #project_id = tracking.get_project_id(project_name)

            #print(result_list)
            if (total_cost == '' and start_date == '' and end_date == ''):
                project_name_save=project_name
                flag = 1
            else:
                result_dict = {"project_id": '', "project_name": '',"project_name_raw":'', "approval_date": '', "sponsoring_ministry": '',
                               "executing_agency": '', "planning_division": '', "cost_unit": '', "project_cost": '',
                               "project_cost_lakh": 0.00, "gob_cost": '', "gob_cost_lakh": 0.00, "pa_cost": '',
                               "pa_cost_lakh": 0.00, "own_fund": '', "own_fund_lakh": 0.00, "start_date": '',
                               "start_month": '', "start_year": '', "end_date": '', "end_month": '', "end_year": '',
                               "project_activity": '', "project_purpose": '', "project_location": []}
                total_cost=total_cost.replace(',','')
                mo = rules.cost_value_re.search(total_cost)
                cost = mo.group(0)
                idx = total_cost.find(cost)
                cost_unit = total_cost[idx + len(cost):]
                if(project_name_save!=''):
                    result_dict['project_name']= project_name_save
                    result_dict['project_id']= project_id
                    result_dict['approval_date']= approval_date
                    result_dict['project_cost']= cost
                    result_dict['cost_unit']= cost_unit
                    result_dict['start_date']= start_date
                    result_dict['end_date']= end_date
                    result_dict['planning_division']= division
                else:
                    result_dict['project_name'] = project_name
                    result_dict['project_id'] = project_id
                    result_dict['approval_date'] = approval_date
                    result_dict['project_cost'] = cost
                    result_dict['cost_unit'] = cost_unit
                    result_dict['start_date'] = start_date
                    result_dict['end_date'] = end_date
                    result_dict['planning_division'] = division

                print(result_dict)
                # if str(p_id)==str(project_id):
                result_list.append(result_dict)
                flag=0
        for data in values:
            if ('Meeting Date' in data):
                #print(data)
                idx = data.find(':')
                approval_date = data[idx + 1:]
                approval_date_key=str(key)

            if (not (rules.division_re.search(data) == None) and flag == 0):
                #print(data)
                idx=data.find(':')
                #print(idx)
                if(idx<6):
                    data=data[idx+1:]
                    idx=data.find(':')
                division=data[:idx]
                print(division)
                flag = 1
                continue

    #print(result_list)
        #print(data)
    return result,result_list


def extract_other(data_list):
    try:
        project_name=data_list[0]
        total_cost=''
        start_date=''
        end_date=''
        #print(project_name)
        for data in data_list:
            #print(data)
            if(not (rules.estimated_cost_re.search(data) == None)):
                print(data)
                mo1=rules.total_re.search(data)
                if(mo1==None):
                    mo1=rules.total_suplimentary_re.search(data)
                mo2=rules.and_re.search(data)
                total=mo1.group(0)
                idx1 = data.find(total)
                if (mo2 == None):
                    idx2=len(data)
                else:
                    and_v=mo2.group(0)
                    idx2 = data.find(and_v)
                l1=len(total)
                total_cost=data[idx1+l1:idx2]
                #print(total_cost)
            if(not (rules.project_date_re.search(data) == None)):
                #print(data)
                mo1=rules.project_date_re.search(data)
                key1=mo1.group(0)
                idx1 = data.find(key1)
                if(not (rules.from_re.search((data))==None)):
                    mo2 = rules.from_re.search((data))
                    key2 = mo2.group(0)
                    idx2 = data.find(key2)
                    start_date = data[idx1 + len(key1):idx2]
                    end_date = data[idx2 + len(key2):]
                else:
                    mo3 = rules.year_re.search(data[idx1:])
                    year1 = mo3.group(0)
                    year2 = mo3.group(1)
                    idx2 = data.find(year1)
                    start_date = data[idx1 + len(key1):idx2 + len(year1)]
                    end_date = data[idx2 + len(year1) + 1:]

                #print(start_date)
                #print(end_date)

        return project_name,total_cost,start_date,end_date
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())

def extract_brief_summary(operational_data,raw_data):
    try:
        #print("project:")
        result_dict={"project_id":'',"project_name":'','project_name_raw':'',"approval_date":'',"sponsoring_ministry":'',"executing_agency":'',"planning_division":'',"cost_unit":'',"project_cost":'',"project_cost_lakh":0.00,"gob_cost":'',"gob_cost_lakh":0.00,"pa_cost":'',"pa_cost_lakh":0.00,"own_fund":'',"own_fund_lakh":0.00,"start_date":'',"start_month":'',"start_year":'',"end_date":'',"end_month":'',"end_year":'',"project_activity":'',"project_purpose":'',"project_location":[]}
        project_purpose=''
        project_location=[]
        project_activity=''
        flag=''
        lock=0
        for key,value in sorted(operational_data.items()):
            #print(key,value)
            length=len(value)
            if(not rules.date_formate_re.search(value)==None and not rules.approval_date_re.search(value)==None):
                mo=rules.date_formate_re.search(value)
                result_dict['approval_date']=mo.group(0)
            elif (rules.division_re.match(value)):
                #print(value)
                #idx = value.find(':')
                #print(idx)
                result_dict['planning_division'] = value
                # print(result_dict)
            elif(rules.project_name_re.match(value)):
                flag='p_name'
                continue
            elif(flag=='p_name'):
                result_dict['project_name']=value
                result_dict['project_name_raw']=raw_data[key]
                flag=''
            elif(rules.ministy_re.match(value)):
                flag='ministry'
                continue
            elif(flag=='ministry'):
                result_dict['sponsoring_ministry']=value
                flag=''
            elif (rules.agency_re.match(value)):
                flag = 'agency'
                continue
            elif (flag == 'agency'):
                result_dict['executing_agency'] = value
                flag = ''
            elif (rules.objective_re.match(value)):
                flag = 'purpose'
                continue
            elif(flag=='purpose' and rules.stop_point_re.match(value) and len(value)<5):
                result_dict['project_purpose']=project_purpose
                flag=''
            elif (flag == 'purpose'):
                 project_purpose+=  value+ "\n"
            elif (rules.location_re.match(value)):
                flag = 'location'
                continue
            elif(flag=='location' and rules.stop_point_re.match(value) and len(value)<5):
                result_dict['project_location']=project_location
                flag=''
            elif (flag == 'location'):
                 project_location.append(value)
            elif (rules.date_re.match(value) and length<50):
                flag = 'date'
                continue
            elif (flag == 'date'):
                #print(value)
                if(not rules.exception_re.search(value)==None):
                    result_dict['start_date'],result_dict['end_date']=extract_date(operational_data)
                    flag=''
                    continue
                if(not rules.from_re.search(value)==None):
                    mo1=rules.from_re.search(value)
                    break_point = mo1.group(0)
                    idx = value.find(break_point)
                    result_dict['start_date'] = value[:idx]
                    result_dict['end_date'] = value[idx + len(break_point):]
                else:
                    mo = rules.year_re.search(value)
                    year = mo.group(0)
                    idx = value.find(year)
                    result_dict['start_date'] = value[:idx]
                    result_dict['end_date'] = value[idx + len(year):]
                flag = ''
            elif (rules.activity_re.match(value)):
                flag = 'activity'
                continue
            elif (flag == 'activity'):
                result_dict['project_activity']= value
                flag=''
            elif(rules.total_re.match(value)):
                flag='total'
                continue
            elif(flag=='total' and not rules.exception_re.search(value)==None):
                result_dict['cost_unit'],result_dict['project_cost'],result_dict['gob_cost'],result_dict['pa_cost'],result_dict['own_fund']=extract_cost(operational_data)
                lock=1
            elif(flag=='total' and not lock and rules.cost_value_re.match(value)):
                co=rules.cost_value_re.search(value)
                cost=co.group(0)
                result_dict['project_cost']=cost
                idx=value.find('টাকা')
                result_dict['cost_unit']=value[len(cost):idx]+'টাকা'
                flag=''
            elif (rules.gob_cost_re.match(value) and not lock):
                flag = 'gob'
                continue
            elif (flag == 'gob' and rules.stop_point_re.match(value) and len(value) < 5):
                flag = ''
            elif (flag == 'gob' and rules.cost_value_re.match(value)):
                co = rules.cost_value_re.search(value)
                cost = co.group(0)
                result_dict['gob_cost'] = cost
                flag = ''
            elif (rules.pa_cost_re.match(value) and not lock):
                flag = 'pa'
                continue
            elif(flag=='pa' and rules.stop_point_re.match(value) and len(value) < 5):
                flag=''
            elif (flag == 'pa' and rules.cost_value_re.match(value)):
                co = rules.cost_value_re.search(value)
                cost = co.group(0)
                result_dict['pa_cost'] = cost
                flag = ''
            elif (rules.own_fund_re.match(value) and not lock):
                flag = 'own'
                continue
            elif(flag=='own' and rules.stop_point_re.match(value) and len(value) < 5):
                flag=''
            elif (flag == 'own' and rules.cost_value_re.match(value)):
                co = rules.cost_value_re.search(value)
                cost = co.group(0)
                result_dict['own_fund'] = cost
                flag = ''

        #print(result_dict)
        return result_dict
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        data_dict={}
        return data_dict


def extract_date(operational_dict):
    flag=0
    lock=0
    back_track=0
    start_date=''
    end_date=''
    for key,value in operational_dict.items():
        #print(value)
        if(not rules.project_date_re.search(value)==None):
            flag=1
        elif(flag==1 and not rules.exception_re.search(value)==None):
            flag=2
            print(key,value)
        elif(flag==2 and not rules.extension_re.search(value)==None):
            lock=1
            back_track+=2
            print(key, value)
        elif(flag==2 and not rules.approved_re.search(value)==None):
            lock=2
            flag=3
            back_track+=1
            print(key, value)
        elif(flag==3 and back_track>=2 and not rules.from_re.search(value)==None):
            back_track-=1
            continue
        elif(flag==3 and back_track==1 and not rules.from_re.search(value)==None):
            print(key,value)
            mo1 = rules.from_re.search(value)
            break_point = mo1.group(0)
            idx = value.find(break_point)
            start_date = value[:idx]
            end_date = value[idx + len(break_point):]
            flag=0
    print("date:")
    print(start_date,end_date)
    return start_date,end_date

def extract_cost(operation_data):
    cost_unit=''
    project_cost=''
    gob=''
    pa=''
    own=''
    flag=0
    lock=0
    for key,value in operation_data.items():
        if(rules.total_re.match(value)):
            flag=1
        elif(flag==1 and rules.approved_re.match(value)):
            flag=2
        elif(flag==2 and rules.cost_value_re.match(value)):
            co=rules.cost_value_re.search(value)
            cost=co.group(0)
            project_cost=cost
            idx=value.find('টাকা')
            cost_unit=value[len(cost):idx]+'টাকা'
            flag=3
        elif(flag==3 and rules.gob_cost_re.match(value)):
            flag=4
            lock=1
        elif (flag == 4 and rules.stop_point_re.match(value) and len(value) < 5 and not rules.null_cost_re.match(value)):
            flag =0
        elif (flag == 4 and lock == 1 and rules.cost_value_re.match(value)):
            lock=0
            continue
        elif (flag == 4 and lock==0 and rules.cost_value_re.match(value)):
            co = rules.cost_value_re.search(value)
            cost = co.group(0)
            gob= cost
            flag = 0
        elif (rules.pa_cost_re.match(value)):
            flag = 5
            lock=1
            continue
        elif (flag == 5 and rules.stop_point_re.match(value) and len(value) < 5 and not rules.null_cost_re.match(value)):
            flag = 0
        elif (flag == 5 and lock == 1 and rules.cost_value_re.match(value)):
            lock = 0
            continue
        elif (flag == 5 and lock == 0 and rules.cost_value_re.match(value)):
            co = rules.cost_value_re.search(value)
            cost = co.group(0)
            pa = cost
            flag = 0
        elif (rules.own_fund_re.match(value)):
            flag = 6
            lock=1
            continue
        elif (flag == 6 and rules.stop_point_re.match(value) and len(value) < 5 and not rules.null_cost_re.match(value)):
            flag = 0
        elif (flag == 6 and lock == 1 and rules.cost_value_re.match(value)):
            lock = 0
            continue
        elif (flag == 6 and lock == 0 and rules.cost_value_re.match(value)):
            co = rules.cost_value_re.search(value)
            cost = co.group(0)
            own = cost
            flag = 0
    print(cost_unit,project_cost,gob,pa,own)
    return cost_unit,project_cost,gob,pa,own


























