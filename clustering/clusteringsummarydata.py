import dataExtraction.rulesfile.summaryrules as rules
from pprint import pprint

def first_level_clustering(data_dict):
    clusterd_data={}
    cluster_flag = 0
    for key,data in sorted(data_dict.items()):
        #print(key,data)
        if(not (rules.date_formate_re.search(data)==None) and 'একনেক' in data):
            mo=rules.date_formate_re.search(data)
            date=mo.group(0)
            print('here date:')
            print(date)
            clusterd_data[key]='Meeting Date: '+ date
        if(not (rules.division_re.search(data)== None) and cluster_flag==0):
            cluster_flag=1
            clusterd_data[key]=data
            #print(data)
        elif(cluster_flag==1):
            #print(data)
            clusterd_data[key]=data
            cluster_flag=2
        elif (cluster_flag == 2):
            #print(data)
            clusterd_data[key] = data
            cluster_flag = 0

    return clusterd_data

def second_level_clustering(data_dict):
    clusterd_data={}
    temp_list=[]
    key_save=0
    for key, data in sorted(data_dict.items()):
        clusterd_data[key]=[]
        #print(data)
        if(len(data)<50):
            clusterd_data.setdefault(key, []).append(data)
        elif(not rules.activity_re.search(data)==None):
            clusterd_data.setdefault(key_save, []).append(data)
        else:
            values=spliting_data(data)
            for value in values:
                clusterd_data.setdefault(key, []).append(value)
            key_save=key
    #pprint(clusterd_data)
    return clusterd_data

import re
def spliting_data(data):
    data_list_1=[]
    data_list=re.split(r'(।|:(\s)|\[|\]|\.(\s))', data)
    #print(data_list)
    for d in data_list:
        if(len(str(d))>5):
            data_list_1.append(d)
    return data_list_1








































