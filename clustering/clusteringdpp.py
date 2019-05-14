import traceback
import dataExtraction.datapreprocessing.parser as parser
import dataExtraction.datapreprocessing.stopword as stopword
import dataExtraction.rulesfile.clusteringrules as rules
import dataExtraction.rulesfile.rules as dpprules
from pprint import pprint
import dataExtraction.datapreprocessing.processingdata as dataprocessing


def find_projectorg_data(converted_data_dict):
    firstlevel_cluster_data= cluster_orgdata_level1(converted_data_dict)
    #print(firstlevel_cluster_data)
    final_clustered_data= cluster_orgdata_level2(firstlevel_cluster_data)
    #print('final data:\n')
    #print(final_clustered_data)
    return  final_clustered_data

def cluster_orgdata_level1(data_dict):
    try:
        json_data = []
        clustered_data = {}
        back_track = 0
        org_flag=0
        lock_key=0
        lock_data=''
        for key,data in sorted(data_dict.items()):
            #print(key,data)
            back_track -= 1
            if(back_track>0):
                clustered_data[key]=data
            if (not (dpprules.ministy_re.search(data) == None)):
                mo = dpprules.ministy_re.search(data)
                sponsoring_ministry_key = mo.group(0)
                #print(sponsoring_ministry_key)
                #org_flag=1
                clustered_data[key]=data
                back_track=17
        return clustered_data

    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None


def cluster_orgdata_level2(data_dict):
    try:
        json_data = []
        clustered_data = {}
        back_track = 0
        org_flag=0
        lock_start_key=0
        lock_end_key=0
        for key,data in sorted(data_dict.items()):
            #print(key,data)
            if (not (dpprules.ministy_re.search(data) == None)):
                lock_start_key=key
            if(not (dpprules.trackorg_re.search(data) == None) and lock_start_key !=0):
                lock_end_key=key
                break

        for key,data in sorted(data_dict.items()):
            if(key>=lock_start_key and key<lock_end_key):
                if((not (dpprules.point_re.search(data) == None) and len(data)<5) or len(data)<5):
                    continue
                clustered_data[key]=data

        #del data_dict
        return clustered_data

    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None


def summarize_dpp(converted_data):
    cleaned_cluster_data={}
    raw_cluster_data={}
    flag=0
    back_track=0
    lock=0
    #print("cleaded data")
    for key,value in sorted(converted_data.items()):
        cleaned = dataprocessing.cleaning_data(value)
        print(key,cleaned)
        #print(cleaned)
        back_track-=1
        if(not (rules.project_name_re.search(cleaned)==None) and flag==0 and lock==0):
            cleaned_cluster_data[key]=cleaned
            raw_cluster_data[key]=value
            flag=1
            back_track=5
            continue
        elif (not (rules.ministry_re.search(cleaned) == None) and flag == 1 and lock==0):
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
            flag = 2
            back_track=15
            continue
        elif(flag==1 and back_track>=0 and lock==0):
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
        elif (not (rules.objective_re.search(cleaned)==None) and lock==0):
            print("objective")
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
            flag = 10
            back_track=20
            continue
        elif(not (rules.date_re.search(cleaned)==None) and lock==0):
            print('date')
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
            flag = 3
            back_track=30
            continue
        elif (not (rules.stop_objective_re.search(cleaned)) == None):
            print('stop obj')
            flag = 0
            lock=1
        elif (flag == 2 and back_track>=0 and lock==0):
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
        elif (flag == 10 and back_track > 0 and lock==0):
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
        elif(not rules.activity_re.search(cleaned)==None):
            flag=25
            lock=0
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
            back_track=50
        elif (not (rules.project_cost_re.search(cleaned) == None) and lock==0):
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
            flag = 4
            back_track = 30
        elif (flag == 3 and back_track >= 0 and lock==0):
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
        elif (not (rules.type_re.search(cleaned) == None) and flag == 4):
            flag=0
        elif (flag == 4 and back_track >= 0 and lock==0):
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
        elif(not (rules.geo_stop_re.search(cleaned)==None) and (rules.not_geo_re.search(cleaned)==None)):
            #print("adsafhsd")
            flag=0
            continue
        elif (not (rules.geo_re.search(cleaned) == None) and len(cleaned)<20 and lock==0):
            #print('geo')
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
            flag = 5
            back_track = 80
        elif (not (rules.geo_stop_re.search(cleaned) == None) and flag == 5):
            #print("afsf")
            flag=0
            continue
        elif(flag==5 and back_track>=0 and lock==0):
            #print('pagapaga')
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
        elif(flag==25 and back_track>0 and lock==0):
            cleaned_cluster_data[key] = cleaned
            raw_cluster_data[key] = value
        elif(back_track<0):
            flag=0


    #pprint(cleaned_cluster_data)
    #pprint(raw_cluster_data)
    return raw_cluster_data,cleaned_cluster_data




def final_level_summarize_dpp(raw_data,cleaned_data):
    current_key=0
    flag=0
    for key,value in sorted(cleaned_data.items()):
        '''if(not (rules.project_name_re.search(value)==None)):
            flag=10
            continue
        elif(flag==10 and len(value)>50):
            flag=0
            continue
        elif(flag==10 and len(value)<50):
            del cleaned_data[key]'''
        if(not (rules.final_clustering_re.search(value)==None) and flag==0 and len(value)<50):
            current_key=key
            flag=1
            continue
        elif(flag==1 and key-current_key<30):
            current_key=key
            continue
        elif(flag==1 and key-current_key>30):
            del cleaned_data[key]
            del raw_data[key]
            continue
        else:
            continue
    return raw_data,cleaned_data




def summarize_dpp_summary(converted_data):
    cluster_data={}
    for key,value in sorted(converted_data.items()):
        cleaned=dataprocessing.cleaning_data(value)
        print(key,cleaned)






























