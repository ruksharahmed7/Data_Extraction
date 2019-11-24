import pandas as pd
import json
from pprint import pprint
import traceback

import dataExtraction.extractionstrategy.extractdpp.projectname as projectname
import dataExtraction.extractionstrategy.extractdpp.estimatedcost as estimatedcost
import dataExtraction.extractionstrategy.extractdpp.projectdate as projectdate
import dataExtraction.extractionstrategy.extractdpp.projectorg as projectorg
import dataExtraction.clustering.clusteringdpp as clusteringdpp
import dataExtraction.clustering.KNNKmeansClassification as KNNKmeansClassification
import dataExtraction.clustering.clusteringsummarydata as clusteringsummarydata
import dataExtraction.clustering.clusteringmeetingminute as clusteringmeetingminute
import dataExtraction.extractionstrategy.extractsummary.summarydetails as summarydetails
import dataExtraction.extractionstrategy.extractmeetingminute.meetingminutedetails as meetingminutedetails
import dataExtraction.extractionstrategy.extractdpp.dppdetails as dppdetails
import dataExtraction.extractionstrategy.extractdpp.projectlocationtableformat as pro_location


import dataExtraction.extractionstrategy.extractdpp.dppextraction as dppextraction
import dataExtraction.resultanalysis.filterdppresult as filterdppresult
import dataExtraction.tracking.filterproject as filter
import  dataExtraction.resultanalysis.converter as Converter
import dataExtraction.resultanalysis.mapping as mapping

def classification_model(train_data_list,train_converted_data_dict,test_data):
    #clusteringdpp.summarize_dpp(converted_data_dict)
    knn,kmean=KNNKmeansClassification.train_data(train_converted_data_dict)
    KNNKmeansClassification.test_model(knn,kmean,test_data)


def clustering_and_get_merge_dpp(raw_data,converted_data,project_id):
    result=[]
    filtered_final_result={}
    #pprint(converted_data)
    raw_cluster_data,cleaned_cluster_data=clusteringdpp.summarize_dpp(converted_data)
    #print("summarized dpp")
    #pprint(raw_cluster_data)
    raw_final_clustered_data,final_clustered_data=clusteringdpp.final_level_summarize_dpp(raw_cluster_data,cleaned_cluster_data)
    print('final cluster')
    pprint(raw_final_clustered_data)
    #result_list=dppdetails.extract_all(raw_cluster_data,cleaned_cluster_data,project_id)
    #print(result_list)
    object_extraction = dppextraction.extractdpp(raw_data, converted_data,raw_cluster_data,cleaned_cluster_data,raw_final_clustered_data, final_clustered_data,project_id)
    object_extraction.extraction_first_level()
    final_result,results=object_extraction.get_results()
    print('final result')
    pprint(final_result)
    print('results')
    pprint(results)
    filtered_final_result,filter_mask=filterdppresult.filter(final_result,results)
    print('filter result')
    pprint(filtered_final_result)
    print(filter_mask)
    object_extraction.set_mask(filter_mask)
    object_extraction.set_final_result(filtered_final_result)
    second_level_results=object_extraction.extraction_second_level()
    pprint(second_level_results)
    final_result = object_extraction.get_final_results()
    print('Finally')
    pprint(final_result)
    print('converting start')
    filtered_final_result=Converter.convertAll(filtered_final_result)
    result.append(filtered_final_result)
    result = mapping.map(result[0])
    json_result = json.dumps(
        result,
        default=lambda df: json.loads(df.to_json()))
    return json_result

def merge_location(result,location_data):
    result=json.loads(result)
    print(result)
    if(not location_data==None):
        location_data=pro_location.convert_location(location_data)
        result[0]['project_location_tab']=location_data
        json_result = json.dumps(
            result,
            default=lambda df: json.loads(df.to_json()))
        return json_result
    else:
        result[0]['project_location_tab']={}
        json_result = json.dumps(
            result,
            default=lambda df: json.loads(df.to_json()))
        return json_result

def clustering_and_get_merge_dpp_summary(raw_data,converted_data,project_id):
    result=[]
    pprint(converted_data)
    clusteringdpp.summarize_dpp_summary(converted_data)



def get_merge_summary(raw_data, converted_data,project_id,project_name):
    try:
        first_cluster= clusteringsummarydata.first_level_clustering(converted_data)
        #pprint(first_cluster)
        second_cluster= clusteringsummarydata.second_level_clustering(first_cluster)
        print('final cluster')
        pprint(second_cluster)
        '''for key,values in sorted(second_cluster.items()):
            print(key)
            for value in values:
                print(value)'''
        result_df,result_list= summarydetails.summary_extract(second_cluster,raw_data)
        print('results')
        pprint(result_list)
        if not result_list:
            print("empty result")
            cluster_data = clusteringsummarydata.clustering_brief_summary(converted_data)
            pprint(cluster_data)
            data_dict={}
            for project_data in cluster_data:
                data_dict=summarydetails.extract_brief_summary(project_data,raw_data)
                print(data_dict)
                if not data_dict:
                    continue
                result_list.append(data_dict)
        pprint(result_list)
        filtered_result=filter.filtering_project_name(result_list,project_name,project_id)
        pprint(filtered_result)
        if(filtered_result==None):
            print("brief summary")
            cluster_data = clusteringsummarydata.clustering_brief_summary(converted_data)
            pprint(cluster_data)
            for project_data in cluster_data:
                result_list.append(summarydetails.extract_brief_summary(project_data,raw_data))
            #pprint(result_list)
            filtered_result = filter.filter_project(result_list, project_name, project_id)
            pprint(filtered_result)
        filtered_convert_result = Converter.convertAll_summary(filtered_result[0])
        result=[]
        result.append(filtered_convert_result)
        result = mapping.map(result[0])

        merge_df = json.dumps(
            result,
            default=lambda df: json.loads(df.to_json()))
        return merge_df
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None





def get_merge_meetingminute(raw_data,converted_data,project_id,project_name):
    first_level_cluster_data_list=clusteringmeetingminute.mm_clustering(converted_data)
    print('mm_cluster')
    pprint(first_level_cluster_data_list)
    ministry_project_cluster=clusteringmeetingminute.ministry_project_clustering(converted_data)
    #pprint(ministry_project_cluster)
    #second_level_cluster_data=clusteringmeetingminute.second_level_clustering(first_level_cluster_data_list)
    #pprint(second_level_cluster_data)
    mmdetails=meetingminutedetails.Meetingminute(raw_data,converted_data,first_level_cluster_data_list,ministry_project_cluster)
    mmdetails.extract_all()
    print("extraction done")
    result_list=mmdetails.get_result()
    print('total project:',len(result_list))
    pprint(result_list)
    filtered_result=filter.filter_project(result_list,project_name,project_id)
    print("filtered result")
    #pprint(filtered_result)
    if(filtered_result):
        filtered_result=Converter.convertMM(filtered_result[0])
        filtered_result=mapping.map(filtered_result[0])
    #pprint(mmdetails.get_result())
    json_result = json.dumps(
        filtered_result,
        default=lambda df: json.loads(df.to_json()))
    #mmdetails.clear_result()
    return json_result


def filter_result(result_list,project_id):
    print('inside filter')
    for result in result_list:
        p_id=result.get("project_id")
        #print(p_id)
        if(str(p_id)==str(project_id)):
            print('id match',p_id)
            return result
    return None










