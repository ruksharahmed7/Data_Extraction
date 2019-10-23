import traceback

import dataExtraction.rulesfile.meetingminuterules as rules
from pprint import pprint

def ministry_project_clustering(data_dict):
    try:
        cluster_data={}
        cluster_data_list={}
        flag=0
        for key,value in data_dict.items():
            if(flag==0 and not rules.ministry_start_re.search(value)==None and len(value)<150):
                flag=1
            elif(flag==1 and not rules.ministry_start_re.search(value)==None):
                flag=0
                break
            elif(flag==1):
                cluster_data[key]=value
        return cluster_data
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())



def mm_clustering(data_dict):
    cluster_data={}
    clustered_data_list=[]
    prev_key=0
    prev_value=''
    next_key = 0
    next_value = ''
    flag=0
    for key,value in sorted(data_dict.items()):
        print(key,value)
        if(not rules.start_re.search(value)==None and flag==0 ):
            print('first')
            cluster_data[key]=value
            flag=11
        elif(flag==11 and not rules.catch_re.search(value)==None):
            cluster_data[key]=value
            # cluster_data[prev_key] = prev_value
            # cluster_data[next_key] = next_value
            print("catch")
            flag=12
            if(len(value)>200):
                flag=5
            continue
        elif(flag==11):
            cluster_data[key]=value
            # next_key=key
            # next_value=value
        elif(flag==12):
            print('sdfhsdjfj')
            cluster_data[key]=value
            flag=5
        elif (not (rules.decision_re.search(value) == None) and flag==5):
            flag=1
            cluster_data[key] = value
            print('found')
            continue
        elif(flag==1 and not rules.approved_re.search(value)==None):
            cluster_data[key]=value
            clustered_data_list.append(cluster_data)
            cluster_data = {}
            flag = 0
        # elif(flag==1 and '(খ)' in value):
        #     clustered_data_list.append(cluster_data)
        #     cluster_data={}
        #     flag=0
        # elif(flag==1 and '(গ)' in value):
        #     clustered_data_list.append(cluster_data)
        #     cluster_data = {}
        #     flag=0
    return clustered_data_list


def first_level_clustering(data_dict):
    cluster_data={}
    flag=0
    for key,value in sorted(data_dict.items()):
        print(key,value)
        if (not (rules.decision_re.search(value) == None) and flag==0):
            flag=1
            cluster_data[key] = value
            print('found')
            continue
        if(flag==1 and '(ক)' in value):
            cluster_data[key]=value
        elif(flag==1 and '(খ)' in value):
            cluster_data[key] = value
        elif(flag==1 and '(গ)' in value):
            cluster_data[key] = value
        else:
            flag=0
    return cluster_data

def second_level_clustering(data_dict):
    cluster_data = {}
    flag = 0
    for key, value in sorted(data_dict.items()):
        #print(key, value)
        str=preprocessing(value)
        if(str):
            #print(str)
            cluster_data[key]=str


    return cluster_data

def preprocessing(str):
    start=0
    end=0
    start=str.find('“')
    end=str.find(
                 'হল।')
    if(start<=0):
        start=str.find('"')
    if(end<=0):
        end=str.find('হলো।')
    #print(start,end)
    if(start>0 and end>0):
        #print(str[start:end+3])
        return str[start:end+3]
    else:
        return False