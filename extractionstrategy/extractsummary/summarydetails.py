import dataExtraction.rulesfile.summaryrules as rules
import dataExtraction.datapreprocessing.processingdata as getcleandata
import pandas as pd
import traceback
import time
from pprint import pprint
import dataExtraction.tracking.trackingprojectid as tracking

def summary_data(clustered_data):
    result_list=[]
    result_dict={}
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
                total_cost=total_cost.replace(',','')
                mo = rules.cost_value_re.search(total_cost)
                cost = mo.group(0)
                idx = total_cost.find(cost)
                cost_unit = total_cost[idx + len(cost):]
                if(project_name_save!=''):
                    result_dict = {'project_name': project_name_save,
                                   'project_id': project_id,
                                   'approval_date': approval_date,
                                   'project_cost': cost,
                                   'cost_unit': cost_unit,
                                   'start_date': start_date,
                                   'end_date': end_date,
                                   'division': division,
                                   'confidence_level': confidence_level,
                                   'location_index': approval_date_key + ',' + str(key)}
                else:
                    result_dict = {'project_name': project_name,
                                   'project_id': project_id,
                                   'approval_date': approval_date,
                                   'project_cost': cost,
                                   'cost_unit': cost_unit,
                                   'start_date': start_date,
                                   'end_date': end_date,
                                   'division': division,
                                   'confidence_level': confidence_level,
                                   'location_index': approval_date_key + ',' + str(key)}

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




























