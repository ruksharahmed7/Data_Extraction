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

"""
Extraction from DPP
Steps of Algorithm:
Step 1. Summarized DPP
Step 2. Search and retrieve relevant meta-data from summarized data using different tactics
Step 3. Track matching data using mask (bool)
    filter_mask: index 0--> project name
                 index 1--> project cost
                 index 2--> project date
                 index 3--> project organization
                 index 4--> project purpose
                 index 5--> project location
                 index 6--> project activity
Step 4. Check mask result and find the not-found data
Step 5. Search and retrieve not-founded data by using non-summarized data
Step 6. Convert data in proper data format (Cost in Lakh, Date in dd/mm/yyyy or jan'yyyy, Mapping with master data)
Step 7. Return data by transforming json[{}] format
"""
def clustering_and_get_merge_dpp(raw_data,converted_data,project_id):
    result=[]
    filtered_final_result={}
    ###Step 1 ###
    #### Summarized DPP file and cut off the unrelevent data
    raw_cluster_data,cleaned_cluster_data=clusteringdpp.summarize_dpp(converted_data)
    raw_final_clustered_data,final_clustered_data=clusteringdpp.final_level_summarize_dpp(raw_cluster_data,cleaned_cluster_data)
    print('final cluster')
    pprint(raw_final_clustered_data)
    ###Step 2 ###
    ###DPP Extraction Instance initiated
    object_extraction = dppextraction.extractdpp(raw_data, converted_data,raw_cluster_data,cleaned_cluster_data,raw_final_clustered_data, final_clustered_data,project_id)
    object_extraction.extraction_first_level()
    final_result,results=object_extraction.get_results()
    print('final result')
    pprint(final_result)
    print('results')
    pprint(results)
    ### Step 3 ###
    filtered_final_result,filter_mask=filterdppresult.filter(final_result,results)
    print('filter result')
    pprint(filtered_final_result)
    print(filter_mask)
    ### Step 4 ###
    object_extraction.set_mask(filter_mask)
    object_extraction.set_final_result(filtered_final_result)
    ### Step 5 ##
    second_level_results=object_extraction.extraction_second_level()
    pprint(second_level_results)
    final_result = object_extraction.get_final_results()
    print('Finally')
    pprint(final_result)
    print('converting start')
    ### Step 6 ###
    filtered_final_result=Converter.convertAll(filtered_final_result)
    result.append(filtered_final_result)
    result = mapping.map(result[0])
    ### Step 7 ###
    json_result = json.dumps(
        result,
        default=lambda df: json.loads(df.to_json()))
    return json_result

"""
Location in tab format from DPP
"""
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

"""
Extraction from Summary
Steps of Algorithm:
Step 1. Summarized summary and cluster each project, append in a list of dictionary. Each dictionary contains a specific project data
Step 2. For each project data Search and retrieve relevant meta-data from each clustered dictionary
Step 3. If Fist attempt result list is none then confirm it's Brief summary and execute brief summary extraction tactics
Step 4. Filter the input 'project_name' project data from the result list
Step 5. Convert data in proper data format (Cost in Lakh, Date in dd/mm/yyyy or jan'yyyy, Mapping with master data)
Step 6. Return data by transforming json[{}] format
"""

def get_merge_summary(raw_data, converted_data,project_id,project_name):
    try:
        ###Step 1 ##
        first_cluster= clusteringsummarydata.first_level_clustering(converted_data)
        second_cluster= clusteringsummarydata.second_level_clustering(first_cluster)
        print('final cluster')
        pprint(second_cluster)
        '''for key,values in sorted(second_cluster.items()):
            print(key)
            for value in values:
                print(value)'''
        ### Step 2 ###
        result_df,result_list= summarydetails.summary_extract(second_cluster,raw_data)
        print('results')
        pprint(result_list)
        ### Step 3 ###
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
        ### Step 4 ###
        filtered_result=filter.filtering_project_name(result_list,project_name,project_id)
        pprint(filtered_result)
        ### Step 3 again ###
        if(filtered_result==None):
            print("brief summary")
            cluster_data = clusteringsummarydata.clustering_brief_summary(converted_data)
            pprint(cluster_data)
            for project_data in cluster_data:
                result_list.append(summarydetails.extract_brief_summary(project_data,raw_data))
            #pprint(result_list)
            filtered_result = filter.filter_project(result_list, project_name, project_id)
            pprint(filtered_result)
        ### Step 5 ###
        filtered_convert_result = Converter.convertAll_summary(filtered_result[0])
        result=[]
        result.append(filtered_convert_result)
        result = mapping.map(result[0])
        ### Step 6 ###
        merge_df = json.dumps(
            result,
            default=lambda df: json.loads(df.to_json()))
        return merge_df
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None


"""
Extraction from Meeting Minute
Steps of Algorithm:
Step 1. Summarized MeetingMinute and cluster each project, append in a list of dictionary. Each dictionary contains a specific project data
Step 2. For each project data Search and retrieve relevant meta-data from each clustered dictionary
Step 3. Filter the input 'project_name' project data from the result list
Step 4. Convert data in proper data format (Cost in Lakh, Date in dd/mm/yyyy or jan'yyyy, Mapping with master data)
Step 5. Return data by transforming json[{}] format
"""
def get_merge_meetingminute(raw_data,converted_data,project_id,project_name):
    ### Step 1 ###
    first_level_cluster_data_list=clusteringmeetingminute.mm_clustering(converted_data)
    print('mm_cluster')
    pprint(first_level_cluster_data_list)
    ministry_project_cluster=clusteringmeetingminute.ministry_project_clustering(converted_data)
    ### Step 2 ###
    mmdetails=meetingminutedetails.Meetingminute(raw_data,converted_data,first_level_cluster_data_list,ministry_project_cluster)
    mmdetails.extract_all()
    print("extraction done")
    result_list=mmdetails.get_result()
    print('total project:',len(result_list))
    pprint(result_list)
    ### Step 3 ###
    filtered_result=filter.filter_project(result_list,project_name,project_id)
    print("filtered result")
    pprint(filtered_result)
    ### Step 4 ###
    if(filtered_result):
        filtered_result=Converter.convertMM(filtered_result[0])
        filtered_result=mapping.map(filtered_result[0])
    #pprint(mmdetails.get_result())
    ### Step 5 ###
    json_result = json.dumps(
        filtered_result,
        default=lambda df: json.loads(df.to_json()))
    #mmdetails.clear_result()
    return json_result











