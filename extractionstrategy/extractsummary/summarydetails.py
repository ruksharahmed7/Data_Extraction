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
    #pprint(clustered_data)
    for key, values in sorted(clustered_data.items()):
        #print(values)
        if (flag == 1):
            confidence_level=0
            project_name,total_cost,start_date,end_date=extract_other(values)
            #project_id = tracking.get_project_id(project_name)
            if(project_name!='' and total_cost!='' and start_date!='' and end_date!=''):
                confidence_level=1
            dict_data = {'approved_project_'+str(project_id): pd.Series([project_name,approval_date,total_cost,start_date,end_date,confidence_level,approval_date_key+','+ str(key)],
                                                    index=['project_name','approval_date','project_cost','start_date','end_date','confidence_level','location_index'])}

            mo=rules.cost_value_re.search(total_cost)
            cost=mo.group(0)
            idx=total_cost.find(cost)
            cost_unit=total_cost[idx+len(cost):]
            result_dict={'project_name': project_name,
                         'project_id':project_id,
                         'approval_date': approval_date,
                         'project_cost':cost,
                         'cost_unit':cost_unit,
                         'start_date':start_date,
                         'end_date':end_date,
                         'division':division,
                         'confidence_level':confidence_level,
                         'location_index':approval_date_key+','+ str(key)}

            #print(result_dict)
            #if str(p_id)==str(project_id):
            result_list.append(result_dict)
            #print(result_list)
            df1 = pd.DataFrame(dict_data)
            # print(dict_data)
            result = pd.concat([result, df1], axis=1, sort=False)
            #project_track
            dict_data.clear()
            #result_dict.clear()
            del df1
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



def track_project(project_id,project_name):
    cleaned_project_name=getcleandata.cleaning_data(project_name)
    #print(project_name,cleaned_project_name)
    #project_track_dict = {'Tracking project': pd.Series(
     #   [project_id,project_name, cleaned_project_name],
      #  index=['project_id','project_name', 'cleaned_project_name'])}

    project_track_dict = {'project_id':[project_id],'project_name':[project_name],'clean_project_name':[cleaned_project_name]}
    df = pd.DataFrame(project_track_dict,index=[project_id])
    track_list=[project_id,project_name,cleaned_project_name]

    with open('project_track.csv', 'a') as f:
        df.to_csv(f, header=False)

    project_track_dict.clear()
    data = pd.read_csv("project_track.csv")
    #pprint(data)
    del df




























