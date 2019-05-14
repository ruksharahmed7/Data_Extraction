import dataExtraction.rulesfile.meetingminuterules as rules
from pprint import pprint

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