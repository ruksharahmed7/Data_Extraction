import dataExtraction.rulesfile.resultanalysisrules as rules
import numpy as np
from pprint import pprint

def filter(final_result,results):
    filtered_result=[]
    filter_result_dict={}
    track=np.array([1,2,3,4,5,6,7])
    states=[]
    filter_result_dict = final_result[0]
    #pprint(filter_result_dict)
    p_name=filter_result_dict['project_name']
    p_name_en=filter_result_dict['project_name_english']
    temp=results[0]
    if(len(p_name)<10 or len(p_name)>200):
        filter_result_dict['project_name']=temp['project_name']
    if(len(p_name_en)<10 or len(p_name_en)>200):
        for key,value in temp.items():
            if(key=='project_name_eng'):
                filter_result_dict['project_name_english']=temp['project_name_eng']
    states.append(1)
    del temp
    ###project cost
    temp1=results[1]
    temp2=results[2]
    cost_unit=filter_result_dict['cost_unit']
    project_cost=filter_result_dict['project_cost']
    gob_cost=filter_result_dict['gob_cost']
    own_fund=filter_result_dict['own_fund']
    pa_cost=filter_result_dict['pa_cost']
    other_cost=filter_result_dict['other_cost']
    filter_result_dict,flag=cost_filter(filter_result_dict,temp1,temp2,cost_unit,project_cost,gob_cost,own_fund,pa_cost,other_cost)
    if(flag==2):
        states.append(flag)
    del temp1,temp2
    ###project date
    temp1=results[3]
    temp2=results[4]
    start_date=filter_result_dict['start_date']
    end_date=filter_result_dict['end_date']
    filter_result_dict,flag=date_filter(filter_result_dict,temp1,temp2,start_date,end_date)
    if(flag==3):
        states.append(flag)
    del temp1,temp2
    ###project organization
    temp1=results[5]
    #temp2=results[6]
    #pprint(temp1)
    sponsoring_ministry=filter_result_dict['sponsoring_ministry']
    executing_agency=filter_result_dict['executing_agency']
    planning_division=filter_result_dict['planning_division']
    if(len(temp1)>0):
        filter_result_dict,flag=org_filter(filter_result_dict,temp1,sponsoring_ministry,executing_agency,planning_division)
        states.append(flag)
    del temp1
    ###project purpose
    temp=results[6]
    filter_result_dict,msk=project_purpose_filter(filter_result_dict,temp)
    if(msk==1):
        states.append(5)
    del temp
    ###project location
    temp=results[7]
    filter_result_dict,msk=geo_location_filter(filter_result_dict,temp)
    if(msk==1):
        states.append(6)
    ###project activity
    temp=results[8]
    filter_result_dict['project_activity']=temp['project_activity']
    states.append(7)
    #filter_result_dict['project_location'] = temp['project_location']
    #states.append(6)
    #pprint(filter_result_dict)
    #print(states)
    mask=np.in1d(track,states)
    #pprint(mask)
    return filter_result_dict,mask

def cost_filter(filter_result_dict,temp1,temp2,cost_unit,project_cost,gob_cost,own_fund,pa_cost,other_cost):
    #pprint(temp1)
    #pprint(temp2)
    for key,value in temp1.items():
        if (key == 'cost_unit'):
            if (rules.cost_unit_re.search(cost_unit) == None and not (rules.cost_unit_re.search(value) == None)):
                cost_unit = value
        if (key == 'project_cost'):
            if (rules.cost_re.search(project_cost) == None and not (rules.cost_re.search(value) == None)):
                project_cost = value
        if (key == 'gob_cost'):
            if (rules.cost_re.search(gob_cost) == None and not (rules.cost_re.search(value) == None)):
                gob_cost = value
        if(key=='own_fund'):
            if(rules.cost_re.search(own_fund) == None and not (rules.cost_re.search(value) == None) and len(value)>3):
                own_fund=value
        if (key == 'pa_cost'):
            if (rules.cost_re.search(pa_cost) == None and not (rules.cost_re.search(value) == None)):
                pa_cost = value
        if (key == 'other_cost'):
            if (rules.cost_re.search(other_cost) == None and not (rules.cost_re.search(value) == None) and len(value)>3):
                pa_cost = value
    for key,value in temp2.items():
        if (key == 'cost_unit'):
            if (rules.cost_unit_re.search(cost_unit) == None and not (rules.cost_unit_re.search(value) == None)):
                cost_unit = value
        if (key == 'project_cost'):
            if (rules.cost_re.search(project_cost) == None and not (rules.cost_re.search(value) == None)):
                project_cost = value
        if (key == 'gob_cost'):
            if (rules.cost_re.search(gob_cost) == None and not (rules.cost_re.search(value) == None)):
                gob_cost = value
        if (key == 'own_fund'):
            if (rules.cost_re.search(own_fund) == None and not (rules.cost_re.search(value) == None) and len(value)>3):
                own_fund = value
        if (key == 'pa_cost'):
            if (rules.cost_re.search(pa_cost) == None and not (rules.cost_re.search(value) == None)):
                pa_cost = value
        if (key == 'other_cost'):
            if (rules.cost_re.search(other_cost) == None and not (rules.cost_re.search(value) == None) and len(value)>3):
                pa_cost = value
    filter_result_dict['cost_unit']=cost_unit
    filter_result_dict['project_cost']=project_cost
    filter_result_dict['gob_cost']=gob_cost
    filter_result_dict['own_fund']=own_fund
    filter_result_dict['pa_cost']=pa_cost
    filter_result_dict['other_cost']=other_cost
    flag=0
    if(not (rules.cost_unit_re.search(cost_unit) == None) and not (rules.cost_re.search(project_cost) == None) and not (rules.cost_re.search(gob_cost) == None)):
        flag=2
    return filter_result_dict,flag

def date_filter(filter_result_dict,temp1,temp2,start_date,end_date):
    for key,value in temp1.items():
        if(key=='start_date'):
            if (rules.date_re.search(start_date) == None and not (rules.date_re.search(value) == None)):
                start_date=value
        if (key == 'end_date'):
            if (rules.date_re.search(end_date) == None and not (rules.date_re.search(value) == None)):
                end_date = value
    for key,value in temp2.items():
        if(key=='start_date'):
            if (rules.date_re.search(start_date) == None and not (rules.date_re.search(value) == None)):
                start_date=value
        if (key == 'end_date'):
            if (rules.date_re.search(end_date) == None and not (rules.date_re.search(value) == None)):
                end_date = value
    filter_result_dict['start_date']=start_date
    filter_result_dict['end_date']=end_date
    flag=0
    if(not (rules.date_re.search(start_date) == None) and not (rules.date_re.search(end_date) == None)):
        flag=3
    return filter_result_dict,flag


def org_filter(filter_result_dict,temp1,sponsoring_ministry,executing_agency,planning_division):
    #print('inside filter')
    #pprint(temp1)
    for key,value in temp1.items():
        #print(key)
        if(key == "sponsoring_ministry"):
            sponsoring_ministry=value
        if(key == "executing_agency"):
            executing_agency = value
            #pprint(executing_agency)
        if(key == "planning_division"):
            planning_division = value
        else:
            filter_result_dict[key]=value

    filter_result_dict['sponsoring_ministry']=sponsoring_ministry
    filter_result_dict['executing_agency']=executing_agency
    filter_result_dict['planning_division']=planning_division
    flag=4
    return filter_result_dict,flag

def project_purpose_filter(filter_result_dict,temp):
    project_purpose=''
    msk=0
    for key,value in temp.items():
        if(key=='project_purpose'):
            if(len(value)>50 and len(value)<1000):
                filter_result_dict['project_purpose']=value
                msk=1
            else:
                filter_result_dict['project_purpose']=project_purpose
    return filter_result_dict,msk

def geo_location_filter(filter_result_dict,temp):
    project_location = temp['project_location']
    #pprint(project_location)
    filter_result_dict['project_location'] = project_location
    msk = 1

    return filter_result_dict,msk



