import pandas as pd
import json
from pprint import pprint

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

import dataExtraction.extractionstrategy.extractdpp.dppextraction as dppextraction
import dataExtraction.resultanalysis.filterdppresult as filterdppresult
import dataExtraction.tracking.filterproject as filter

def classification_model(train_data_list,train_converted_data_dict,test_data):
    #clusteringdpp.summarize_dpp(converted_data_dict)
    knn,kmean=KNNKmeansClassification.train_data(train_converted_data_dict)
    KNNKmeansClassification.test_model(knn,kmean,test_data)


def clustering_and_get_merge_dpp(raw_data,converted_data,project_id):
    result=[]
    #pprint(converted_data)
    raw_cluster_data,cleaned_cluster_data=clusteringdpp.summarize_dpp(converted_data)
    #pprint(raw_cluster_data)
    raw_final_clustered_data,final_clustered_data=clusteringdpp.final_level_summarize_dpp(raw_cluster_data,cleaned_cluster_data)
    #pprint(raw_final_clustered_data)
    #result_list=dppdetails.extract_all(raw_cluster_data,cleaned_cluster_data,project_id)
    #print(result_list)
    object_extraction = dppextraction.extractdpp(raw_data, converted_data,raw_cluster_data,cleaned_cluster_data,raw_final_clustered_data, final_clustered_data,project_id)
    object_extraction.extraction_first_level()
    final_result,results=object_extraction.get_results()
    #pprint(final_result)
    filtered_final_result,filter_mask=filterdppresult.filter(final_result,results)
    pprint(filtered_final_result)
    print(filter_mask)
    return_result={}
    return_result['approval_date']=filtered_final_result['approval_date']
    return_result['cost_unit']=filtered_final_result['cost_unit']
    return_result['end_date']=filtered_final_result['end_date']
    return_result['executing_agency']=filtered_final_result['executing_agency']
    return_result['gob_cost']=filtered_final_result['gob_cost']
    return_result['other_cost']=filtered_final_result['other_cost']
    return_result['own_fund']=filtered_final_result['own_fund']
    return_result['pa_cost']=filtered_final_result['pa_cost']
    return_result['planning_division']=filtered_final_result['planning_division']
    return_result['project_cost']=filtered_final_result['project_cost']
    return_result['project_id']=filtered_final_result['project_id']
    return_result['project_name']=filtered_final_result['project_name']
    return_result['project_name_english']=filtered_final_result['project_name_english']
    return_result['revised_end_date']=filtered_final_result['revised_end_date']
    return_result['revised_gob_cost']=filtered_final_result['revised_gob_cost']
    return_result['revised_other_cost']=filtered_final_result['revised_other_cost']
    return_result['revised_pa_cost']=filtered_final_result['revised_pa_cost']
    return_result['revised_project_cost']=filtered_final_result['revised_project_cost']
    return_result['revised_start_date']=filtered_final_result['revised_start_date']
    return_result['sponsoring_ministry']=filtered_final_result['sponsoring_ministry']
    return_result['start_date']=filtered_final_result['start_date']
    result.append(return_result)

    json_result = json.dumps(
        result,
        default=lambda df: json.loads(df.to_json()))
    return json_result

def clustering_and_get_merge_dpp_summary(raw_data,converted_data,project_id):
    result=[]
    pprint(converted_data)
    clusteringdpp.summarize_dpp_summary(converted_data)




def get_merge_dpp(data_list, converted_data_dict):
    project_title_json, project_title_df = projectname.extract_project_title_1(data_list)
    # print(project_title_df)
    estimated_cost_json1, estimated_cost_df1 = estimatedcost.extract_estimated_cost_1(data_list)
    # print(json_data2)
    estimated_cost_json2 = []
    estimated_cost_df2 = pd.DataFrame()
    if (len(estimated_cost_json1) < 1):
        estimated_cost_json2, estimated_cost_df2 = estimatedcost.extract_estimated_cost_2(data_list)
        print(estimated_cost_json1)

    peoject_date_json1, project_date_df1 = projectdate.extract_date_1(data_list)
    project_date_df2 = projectdate.extract_date_2(converted_data_dict)

    #project_org_df1 = projectorg.extract_organization_1(converted_data_dict)
    clustered_projectorg_data= clusteringdpp.find_projectorg_cluster(converted_data_dict)
    project_org_df2= projectorg.extract_org_data_1(clustered_projectorg_data)

    frames = [project_title_df, estimated_cost_df1, estimated_cost_df2, project_date_df1, project_date_df2,project_org_df2]
    result = pd.concat(frames, axis=1, sort=False)
    pprint(result)
    merge_df = json.dumps(
        [project_title_df, estimated_cost_df1, estimated_cost_df2, project_date_df1, project_date_df2,project_org_df2],
        default=lambda df: json.loads(df.to_json()))
    #print(merge_df)
    return merge_df

def get_merge_summary(raw_data, converted_data,project_id,project_name):
    first_cluster= clusteringsummarydata.first_level_clustering(converted_data)
    #pprint(first_cluster)
    second_cluster= clusteringsummarydata.second_level_clustering(first_cluster)
    print('final cluster')
    #pprint(second_cluster)
    '''for key,values in sorted(second_cluster.items()):
        print(key)
        for value in values:
            print(value)'''
    result_df,result_list= summarydetails.summary_data(second_cluster)
    filtered_result=filter.filtering_project_name(result_list,project_name,project_id)
    pprint(filtered_result)
    merge_df = json.dumps(
        filtered_result,
        default=lambda df: json.loads(df.to_json()))
    return merge_df


def get_merge_meetingminute(raw_data,converted_data,project_id,project_name):
    first_level_cluster_data=clusteringmeetingminute.first_level_clustering(converted_data)
    #print('cluster')
    #pprint(first_level_cluster_data)
    second_level_cluster_data=clusteringmeetingminute.second_level_clustering(first_level_cluster_data)
    #pprint(second_level_cluster_data)
    mmdetails=meetingminutedetails.Meetingminute(second_level_cluster_data)
    result_df,result_list=mmdetails.get_result()
    pprint(result_list)
    filtered_result=filter.filtering_project_name(result_list,project_name,project_id)
    print("filtered result")
    pprint(filtered_result)
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










