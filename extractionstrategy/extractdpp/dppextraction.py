from pprint import pprint
import dataExtraction.extractionstrategy.extractdpp.dppdetails as dppdetails
import dataExtraction.extractionstrategy.extractdpp.projectname as projectname
import dataExtraction.extractionstrategy.extractdpp.estimatedcost as estimatedcost
import dataExtraction.extractionstrategy.extractdpp.projectdate as projectdate
import dataExtraction.extractionstrategy.extractdpp.projectorg as projectorg
import dataExtraction.extractionstrategy.extractdpp.projectpurpose as projectpurpose
import dataExtraction.extractionstrategy.extractdpp.projectlocation as location
import dataExtraction.extractionstrategy.extractdpp.projectactivity as activity

class extractdpp:
    project_id=''
    results=[]
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
        estimated_cost_json1, estimated_cost_df1,estimated_cost_dict1 = estimatedcost.extract_estimated_cost_1(self.final_clustered_data,self.raw_final_clustered_data)
        pprint(estimated_cost_dict1)
        self.results.append(estimated_cost_dict1)
        estimated_cost_json2, estimated_cost_df2,estimated_cost_dict2 = estimatedcost.extract_estimated_cost_2(self.final_clustered_data,self.raw_final_clustered_data)
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
    def set_mask(self,mask):
        self.filter_mask=mask
        
        
    #def extraction_second_level(self):

        

