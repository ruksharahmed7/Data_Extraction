from pprint import pprint
import dataExtraction.extractionstrategy.extractdpp.dppdetails as dppdetails
import dataExtraction.extractionstrategy.extractdpp.projectname as projectname
import dataExtraction.extractionstrategy.extractdpp.estimatedcost as estimatedcost
import dataExtraction.extractionstrategy.extractdpp.projectdate as projectdate
import dataExtraction.extractionstrategy.extractdpp.projectorg as projectorg
import dataExtraction.extractionstrategy.extractdpp.projectpurpose as projectpurpose
import dataExtraction.extractionstrategy.extractdpp.projectlocation as location
import dataExtraction.extractionstrategy.extractdpp.projectactivity as activity

import dataExtraction.resultanalysis.checkresult as checker
import dataExtraction.resultanalysis.filterdppresult as filter

class extractdpp:
    project_id=''
    results=[]
    second_level_results=[]
    final_result=[]
    raw_data={}
    converted_raw_data={}
    raw_mid_cluster_data={}
    mid_clustered_data={}
    raw_final_clustered_data={}
    final_clustered_data={}
    filter_mask=[]

    def __init__(self,raw_data,converted_raw_data,raw_mid_cluster,mid_level_cluster,raw_final_cluster,final_level_cluster,project_id):
        self.project_id=project_id
        self.raw_data=raw_data
        self.converted_raw_data=converted_raw_data
        self.raw_mid_cluster_data=raw_mid_cluster
        self.mid_clustered_data=mid_level_cluster
        self.raw_final_clustered_data=raw_final_cluster
        self.final_clustered_data=final_level_cluster
        #print("inside class")
        #pprint(self.raw_mid_cluster_data)
        #pprint(self.final_clustered_data)

    def __del__(self):
        print('Destructor called')

    def extraction_first_level(self):
        self.final_result.clear()
        self.results.clear()
        self.final_result=dppdetails.extract_all(self.raw_mid_cluster_data,self.final_clustered_data,self.project_id)
        #pprint(self.results)
        project_name_dict=projectname.extract_project_title_(self.raw_final_clustered_data)
        pprint(project_name_dict)
        self.results.append(project_name_dict)
        estimated_cost_json1, estimated_cost_df1,estimated_cost_dict1 = estimatedcost.extract_estimated_cost_1(self.raw_final_clustered_data)
        print('first function')
        pprint(estimated_cost_dict1)
        self.results.append(estimated_cost_dict1)
        estimated_cost_json2, estimated_cost_df2,estimated_cost_dict2 = estimatedcost.extract_estimated_cost_2(self.raw_final_clustered_data)
        print('2nd function')
        pprint(estimated_cost_dict2)
        self.results.append(estimated_cost_dict2)
        date_df1,date_dict1=projectdate.extract_date_1(self.raw_final_clustered_data)
        pprint(date_dict1)
        self.results.append(date_dict1)
        date_df2, date_dict2 = projectdate.extract_date_2(self.raw_final_clustered_data)
        pprint(date_dict2)
        self.results.append(date_dict2)
        #project_org_df1,project_org_dict1=projectorg.extract_organization1(self.raw_final_clustered_data)
        #self.results.append(project_org_dict1)
        project_org_df2, project_org_dict2 = projectorg.extract_organization_2(self.raw_final_clustered_data)
        self.results.append(project_org_dict2)
        pprint(project_org_dict2)
        #project purspose
        project_purpose_dict=projectpurpose.extract_purpose(self.raw_final_clustered_data)
        self.results.append(project_purpose_dict)
        #geo
        geo_location_dict=location.extract_location(self.raw_final_clustered_data)
        self.results.append(geo_location_dict)
        #pprint(self.results)

        project_activity_dict=activity.extract_activity(self.raw_final_clustered_data)
        self.results.append(project_activity_dict)

    def get_results(self):
        return self.final_result,self.results
    def get_final_results(self):
        return self.final_result
    def set_mask(self,mask):
        self.filter_mask=mask
    def set_final_result(self,filter_result):
        self.final_result.clear()
        self.final_result=filter_result
    def extraction_second_level(self):
        print('second level')
        temp_result=[]
        pprint(self.converted_raw_data)
        #print(self.filter_mask)
        temp_result.clear()
        if (self.filter_mask[0] == False):
            project_name_dict = projectname.extract_project_title_(self.converted_raw_data)
            pprint(project_name_dict)
            temp_result.append(project_name_dict)
        if (self.filter_mask[1]==False):
            try:
                estimated_cost_json1, estimated_cost_df1, estimated_cost_dict1 = estimatedcost.extract_estimated_cost_1(
                    self.converted_raw_data)
                pprint(estimated_cost_dict1)
                temp_result.append(estimated_cost_dict1)
                estimated_cost_json2, estimated_cost_df2, estimated_cost_dict2 = estimatedcost.extract_estimated_cost_2(
                    self.converted_raw_data)
                pprint(estimated_cost_dict2)
                temp_result.append(estimated_cost_dict2)
                self.results.append(estimated_cost_dict1)
                self.results.append(estimated_cost_dict2)
                self.final_result=filter.second_level_cost_append(temp_result, self.final_result)
            except Exception as e:
                print("exception")
                data_dict=estimatedcost.extract_estimated_cost_3(self.converted_raw_data)
        if (self.filter_mask[2]==False):
            print("reverse date")
            try:
                data_df,data_dict=projectdate.extract_date_1(self.converted_raw_data)
                if(checker.check_date(data_dict)):
                    print('found correct date')
                    print(data_dict)
                    self.final_result=filter.second_level_date_append(data_dict,self.final_result)
                else:
                    data_df,data_dict=projectdate.extract_date_1(self.converted_raw_data)
                    print(data_dict)
                    self.final_result = filter.second_level_date_append(data_dict, self.final_result)
            except Exception as e:
                print("exception")
                data_dict=projectdate.extract_date_exception(self.converted_raw_data)
                self.final_result = filter.second_level_date_append(data_dict, self.final_result)
            # date_df1, date_dict1 = projectdate.extract_date_1(self.converted_raw_data)
            # pprint(date_dict1)
            # temp_result.append(date_dict1)
            # date_df2, date_dict2 = projectdate.extract_date_2(self.converted_raw_data)
            # pprint(date_dict2)
            # temp_result.append(date_dict2)
        if(self.filter_mask[3] ==False):
                project_org_df2, project_org_dict2 = projectorg.extract_organization_2(self.converted_raw_data)
                if (checker.check_org(project_org_dict2)):
                    self.final_result = filter.second_level_org_append(project_org_dict2, self.final_result)
                else:
                   project_org_dict = projectorg.extract_organization_3(self.converted_raw_data)
                   self.final_result = filter.second_level_org_append(project_org_dict, self.final_result)
        if (self.filter_mask[4]==False):
            project_purpose_dict = projectpurpose.extract_purpose(self.converted_raw_data)
            self.final_result['project_purpose']=project_purpose_dict['project_purpose']
            print(project_purpose_dict)
        if (self.filter_mask[5]==False):
            project_location_dict = location.extract_location(self.converted_raw_data)
            print('end:',project_location_dict)
            self.final_result=filter.second_level_location_append(project_location_dict,self.final_result)
        if(self.filter_mask[6] ==False):
            project_activity_dict = activity.extract_activity(self.converted_raw_data)
            self.final_result=filter.second_level_activity_append(project_activity_dict,self.final_result)
            print(project_activity_dict)
        self.results+=temp_result
        return self.results



        
        
    #def extraction_second_level(self):

        

