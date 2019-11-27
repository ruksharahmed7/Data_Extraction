import dataExtraction.rulesfile.meetingminuterules as mmrules
import dataExtraction.rulesfile.rules as dpprules
import dataExtraction.datapreprocessing.processingdata as getcleandata
import dataExtraction.tracking.trackingprojectid as tracking
import pandas as pd
import traceback
from pprint import pprint
import nltk
from nltk import RegexpTokenizer
from cltk.tokenize.sentence import TokenizeSentence

word_tokenize = RegexpTokenizer("[\u0980-\u09FF']+")

class Meetingminute:
    result = pd.DataFrame()
    restul_list=[]

    def __init__(self,raw_data,converted_data,cluster_data_list,ministry_cluster_data):
        self.raw_data=raw_data
        self.converted_data=converted_data
        self.cluster_data_list=cluster_data_list
        self.ministry_cluster_data=ministry_cluster_data
        pprint(self.ministry_cluster_data)
        print("Meeting minute Parsing started")

    def get_result(self):
        return self.restul_list

    def clear_result(self):
        self.restul_list.clear()

    def extract_all(self):
        self.restul_list=[]
        self.extract_ecnec_project()
        self.extract_ministry_project()
        #pprint(self.restul_list)

    def extract_ministry_project(self):
        try:
            print("ministry project extraction start")
            pprint(self.ministry_cluster_data)
            project_list=[]
            data_dict={}
            planning_div=''
            ministry=''
            agency=''
            project_name=''
            start_date=''
            end_date=''
            cost=''
            cost_unit=''
            flag=1
            for key,value in self.ministry_cluster_data.items():
                print(key,value)
                print(flag)
                if(flag==1 and not mmrules.div_start.search(value)==None):
                    mo=mmrules.div_start.search(value)
                    div=mo.group(0)
                    planning_div=value[:value.find(div)]
                    print(planning_div)
                    flag=1
                elif(flag==1 and not mmrules.project_start.search(value)==None and len(value)<5):
                    print('start')
                    flag=2
                    continue
                elif(flag==2):
                    project_name=value
                    project_name_key=key
                    print('p_name:',project_name)
                    flag=3
                elif(flag==3 and not mmrules.year_re.search(value)==None):
                    start_date=value
                    print(start_date)
                    flag=4
                # elif(flag==3 and not mmrules.date_mid_point.search(value)==None):
                #     flag=4
                elif(flag==4 and not mmrules.year_re.search(value)==None):
                    end_date=value
                    print(end_date)
                    flag=4
                elif(flag==4 and not mmrules.ministry.search(value)==None):
                    print("ministry")
                    idx=value.find('/')
                    ministry=value[:idx]
                    agency=value[idx+1:]
                    print(ministry,agency)
                    flag=5
                elif(flag==5 and not mmrules.min_estimated_cost.search(value)==None):
                    print('cost')
                    mo1=mmrules.amount_re.search(value)
                    cost=mo1.group(0)
                    print(cost)
                    idx1=value.find(cost)+len(cost)
                    cost_unit=value[idx1:]
                    print(cost,cost_unit)
                    continue
                elif(flag==5 and not mmrules.date_format_re.search(value)==None):
                    data_dict = {"cost_unit": cost_unit,
                                 "end_date": end_date,
                                 "gob_cost": cost,
                                 "is_ministry_project": 1,
                                 "own_fund": '',
                                 "own_fund_type": '',
                                 "pa_cost": '',
                                 "pa_cost_name": '',
                                 "planning_division": planning_div,
                                 "project_activity": '',
                                 "project_benefit": '',
                                 'project_purpose':'',
                                 "project_cost": cost,
                                 "project_id": '',
                                 "project_name": project_name,
                                 "project_name_raw":self.raw_data[project_name_key],
                                 "sponsoring_ministry": ministry,
                                 "executing_agency":agency,
                                 "start_date": start_date,
                                 "approval_date":value
                                 }
                    #pprint(data_dict)
                    project_list.append(data_dict)
                    self.restul_list.append(data_dict)
                    data_dict={}
                    flag=1
            pprint(project_list)
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())




    def extract_ecnec_project(self):
        #pprint(self.cluster_data_list)
        df = pd.DataFrame()
        for clustered_data in self.cluster_data_list:
            prev_key=0
            temp_data_dict = {}
            for key,value in sorted(clustered_data.items()):
                #index=value.find('(ক)')
                if(not mmrules.approved_re.search(value)==None):
                    data_dict={}
                    data_dict,list_formate_data=self.extract(value,key)
                    if(data_dict==None):
                        continue
                    #print(data_dict)
                    df = pd.DataFrame(data_dict)
                    self.result = pd.concat([self.result, df], axis=1, sort=False)
                    #print(list_formate_data)
                    #if str(list_formate_data['project_id'])==str(project_id):
                    #print(temp_data_dict)
                    #print(list_formate_data)
                    list_formate_data.update(temp_data_dict)
                    self.restul_list.append(list_formate_data)
                    pprint(list_formate_data)
                    #pprint(self.restul_list)
                    del df
                if(not mmrules.decision_re.search(value)==None):
                    temp_data_dict=self.extract_other(clustered_data[prev_key])
                else:
                    prev_key=key
        if(not self.restul_list):
            print("other format")
            for clustered_data in self.cluster_data_list:
                self.restul_list.append(self.extract_second_format(clustered_data))
                #pprint(self.result)

    def extract_other(self,value):
        try:
            data_dict={'sponsoring_ministry':'','planning_division':'','project_activity':'','project_benefit':'','project_purpose':''}
            pprint(value)
            mo1=mmrules.min_start_re.search(value)
            if(not mo1):
                mo1=mmrules.min_start_re_01.search(value)
            min_start = mo1.group(0)
            print(min_start)
            mo2=mmrules.min_end_re.search(value)
            min_end=mo2.group(0)
            print(min_end)
            ministry=value[value.find(min_start)+len(min_start):value.find(min_end)]
            ministry = ministry.replace('মন্ত্রণালয়ের', 'মন্ত্রণালয়')
            ministry = ministry.replace('কার্যালয়ের', 'কার্যালয়')
            data_dict['sponsoring_ministry']=ministry
            #pprint(data_dict)

            mo3 = mmrules.planning_div_start_re.search(value)
            # if (not mo1):
            #     mo1 = mmrules.min_start_re_01.search(value)
            div_start = mo3.group(0)
            print(div_start)
            mo4 = mmrules.planning_div_end_re.search(value)
            div_end = mo4.group(0)
            print(div_end)
            if(mo3 and mo4):
                division = value[value.find(div_start) + len(div_start):value.find(div_end)]
                data_dict['planning_division']=division

            mo5=mmrules.activity_start_re.search(value)
            mo6=mmrules.benefite_start_re.search(value)
            if(not mo6):
                mo6=mmrules.benefite_start_re01.search(value)
            if(mo5 and mo6):
                he_says=mo5.group(0)
                he_again_says=mo6.group(0)
                index1=value.find(he_says)
                index2=value.find(he_again_says)
                value_crop=value[index1:index2]
                print(value_crop)
                # mo7=mmrules.activity_grap_re.search(value_crop)
                # goal=mo7.group(0)
                # print(goal)
                # activitiy_start_idx=value_crop.find(goal)+len(mo7.group(0))
                activitiy_start_idx=0
                activity_end_idx=0
                #activitiy_start_idx=value_crop.find('(')
                mo7=mmrules.activity_grap_re.search(value_crop)
                if(mo7):
                    goal=mo7.group(0)
                    if(len(goal)<7):
                        activitiy_start_idx = value_crop.find(goal)
                    else:
                        activitiy_start_idx = value_crop.find(goal)+len(goal)
                    #goal=mo7.group(0)
                    print(goal)

                print(activitiy_start_idx)
                if(activitiy_start_idx<=0):
                    activitiy_start_idx=len(he_says)+1
                mo8=mmrules.end_activity_re.search(value_crop)
                if(mo8):
                    end = mo8.group(0)
                    activity_end_idx=value_crop.find(end)+len(end)
                else:
                    activity_end_idx=index2-1
                benefit_start_idx=index2+len(he_again_says)+1
                data_dict['project_activity']=value_crop[activitiy_start_idx:activity_end_idx]
                benefit_end_idx=len(value)-1
                mo9=mmrules.benefite_end_re.search(value)
                if(mo9):
                    end_ben=mo9.group(0)
                    benefit_end_idx=value.find(end_ben)+len(end_ben)
                print(benefit_start_idx,benefit_end_idx)
                benefit=value[benefit_start_idx:]
                benefit=self.crop_benefit(benefit)
                data_dict['project_benefit']=benefit

            pprint(data_dict)
            return data_dict
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())
            return data_dict


    def extract(self,data,key):
        try:
            if (not mmrules.unapproved_re.search(data) == None):
                return None,None
            data_dict = {}
            list_formate_data = {}
            project_id=''
            project_name=''
            total_cost=''
            gob_cost=''
            cost_unit=''
            pa_cost=''
            pa_fund_type = ''
            own_fund=''
            own_fund_type=''

            start_date=''
            end_date=''
            confidence_level=1
            print(data)
            project_name,end=self.extract_project_name(data)
            project_name_raw,end_raw=self.extract_project_name(self.raw_data[key])
            print("project:",project_name)

            ###Cost extraction###
            other_data=data[end+2:]
            tokenizer = TokenizeSentence('bengali')
            bengali_text_tokenize = tokenizer.tokenize(data[end+2:])
            #print(bengali_text_tokenize)
            flag=0

            for i in range(len(bengali_text_tokenize)):
                #print(bengali_text_tokenize[i])
                if((bengali_text_tokenize[i]=='সম্পূর্ণ' or bengali_text_tokenize[i]=='সম্পর্ণ') and flag==0):
                    flag=1
                    continue
                if(flag==1 and bengali_text_tokenize[i]=='জিওবি'):
                    flag=2
                    continue
                if(flag==2 and bengali_text_tokenize[i]=='মোট'):
                    total_cost=bengali_text_tokenize[i+1]+bengali_text_tokenize[i+2]+bengali_text_tokenize[i+3]
                    gob_cost=total_cost
                    cost_unit=bengali_text_tokenize[i+4]+' '+bengali_text_tokenize[i+5]
                if(flag==0 and bengali_text_tokenize[i]=='মোট'):
                    total_cost = bengali_text_tokenize[i + 1] + bengali_text_tokenize[i + 2] + bengali_text_tokenize[i + 3]
                    cost_unit = bengali_text_tokenize[i + 4] + ' ' + bengali_text_tokenize[i + 5]
                    flag=3
            ##Other cost extraction##
            # idx1=other_data.find('[')
            # idx2=other_data.find(']')
            # if(idx2==-1):
            #     idx2=other_data.find('প্রাক্কলিত')
            # if(idx1>0 and idx2>0):
            #     gob_cost,pa_cost,pa_fund_type,own_fund,own_fund_type=self.other_cost(other_data[idx1+1:idx2])
            idx=other_data.find(total_cost)
            other_cost_data=other_data[idx+len(total_cost)+len(cost_unit):]
            print(other_cost_data)
            gob_cost,pa_cost,own_fund=self.other_cost(other_cost_data)
            print(gob_cost,pa_cost,own_fund)


            ###End cost Extraction###
            track1=0
            track2=0
            s=0
            if(not (mmrules.track2_re.search(other_data)==None)):
                mid_mo = mmrules.track2_re.search(other_data)
                track1=other_data.find(mid_mo.group(0))
                s=len(mid_mo.group(0))
            else:
                start_mo = mmrules.track1_re.search(other_data)
                txt=start_mo.group(0)
                print(txt)
                track1=other_data.find(txt)
                s=len(txt)
            end_mo = mmrules.track3_re.search(other_data)
            txt1=end_mo.group(0)
            track2=other_data.find(txt1)
            date_data=other_data[track1+s:track2]
            date_data=date_data.strip('ে')
            print(date_data)
            start_date,end_date=self.date_extract(date_data)
            #project_id=tracking.get_project_id(project_name)
            #print(project_name,total_cost, cost_unit, gob_cost, pa_cost, pa_fund_type, own_fund, own_fund_type,start_date,end_date)
            if(gob_cost==''):
                gob_cost=total_cost
            if(cost_unit=='' or len(cost_unit)<3):
                cost_unit='কোটি টাকা'
            list_formate_data = {'project_id':project_id,'project_name': project_name,'project_name_raw':project_name_raw, 'project_cost': total_cost, 'cost_unit': cost_unit,
                         'gob_cost': gob_cost, 'pa_cost': pa_cost, 'pa_cost_name': pa_fund_type, 'own_fund': own_fund,'executing_agency':'',
                         'own_fund_type': own_fund_type,'approval_date':self.get_approval_date(), 'start_date': start_date, 'end_date': end_date,'is_ministry_project':0}
            # pprint(data_dict)

            data_dict = {'approved_project_' + str(project_id): pd.Series(
                [project_name, total_cost,cost_unit,gob_cost,pa_cost,pa_fund_type,own_fund,own_fund_type, start_date, end_date, confidence_level,
                 str(key)],
                index=['project_name', 'total_project_cost','cost_unit','gob_cost', 'pa_fund','pa_fund_name','own_fund','own_fund_name','start_date', 'end_date', 'confidence_level',
                       'location_index'])}
            return data_dict,list_formate_data
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())
            list_formate_data = {'project_id': project_id, 'project_name': project_name,'project_name_raw':project_name_raw, 'project_cost': total_cost,
                                 'cost_unit': cost_unit,
                                 'gob_cost': gob_cost, 'pa_cost': pa_cost, 'pa_cost_name': pa_fund_type,
                                 'own_fund': own_fund, 'executing_agency': '',
                                 'own_fund_type': own_fund_type, 'approval_date': '', 'start_date': start_date,
                                 'end_date': end_date, 'is_ministry_project': 0}

            return data_dict,list_formate_data



    def extract_project_name(self,data):
        try:
            project_name=''
            start_mo = mmrules.project_name_notation.search(data)
            start_notation = start_mo.group(0)
            start_notation_idx = data.find(start_notation)
            data_crop = data[start_notation_idx + len(start_notation):]
            end_mo = mmrules.project_name_notation.search(data_crop)
            end_notation = end_mo.group(0)
            end_notation_idx = data_crop.find(end_notation)
            project_name = data_crop[:end_notation_idx]
            return project_name,end_notation_idx
        except:
            start = data.find('“')
            end = 0
            # print(start)
            if (start == -1):
                start = data.find('"')
                end = data[start + 1:].find('"')
                print(start, end)
                project_name = data[start + 1:end + start + 1]
            else:
                end = data[start + 1:].find('”')
                print(start, end)
                project_name = data[start + 1:end + start + 1]
            return project_name,end

    def date_extract(self,date_data):
        mo=mmrules.break_re.search(date_data)
        txt=mo.group(0)
        idx=date_data.find(txt)
        l=len(txt)
        start_date=date_data[:idx]
        end_date=date_data[idx+l:]
        return start_date,end_date

    def other_cost(self,str):
        # data=[]
        # idx1=str.find(',')
        # if(idx1!=-1):
        #     data.append(str[:idx1])
        #     str=str[idx1+1:]
        # idx2 = str.find('এবং')
        # data.append(str[:idx2])
        # data.append(str[idx2+3:])
        #pprint(data)
        gob_cost=''
        pa_cost=''
        pa_fund_type=''
        own_fund=''
        own_fund_type=''
        last_idx=-1
        # for val in data:
        if(not (mmrules.gob_re.search(str)==None)):
            mo1 = mmrules.gob_re.search(str)
            gob = mo1.group(0)
            idx = str.find(gob)
            mo2 = mmrules.amount_re.search(str[idx:])
            gob_cost=mo2.group(0)
            idx=str.find(gob_cost)
            last_idx=idx+len(gob_cost)
        if(not (mmrules.pa_re.search(str)==None)):
            mo1 = mmrules.pa_re.search(str)
            pa=mo1.group(0)
            idx=str.find(pa)
            mo2=mmrules.amount_re.search(str[idx:])
            pa_cost = mo2.group(0)
            idx=str.find(pa_cost)
            last_idx=idx+len(pa_cost)
        if (not mmrules.amount_re.search(str[last_idx:])==None):
                mo = mmrules.amount_re.search(str[last_idx:])
                own_fund = mo.group(0)
        return gob_cost,pa_cost,own_fund



    def crop_benefit(self,str):
        mo=mmrules.benefite_end_re.search(str)
        if(mo):
            end=mo.group(0)
            idx=str.find(end)+len(end)
            return str[:idx]
        return str



    def get_approval_date(self):
        try:
            approval_date=''
            flag=0
            for key,value in self.converted_data.items():
                if(not mmrules.approval_date_start_re.search(value)==None and flag==0):
                    flag=1
                elif(flag==1 and not mmrules.date_re.search(value)==None):
                    mo=mmrules.date_re.search(value)
                    date=mo.group(0)
                    idx=value.find(date)
                    approval_date=value[:idx]
                    flag=2
            return approval_date
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())
            return approval_date


    def extract_second_format(self,data_dict):
        result_dict={'project_id':'','project_name': '','project_name_raw':'', 'project_cost': '', 'cost_unit': '',
                         'gob_cost': '', 'pa_cost': '', 'pa_cost_name': '', 'own_fund': '','executing_agency':'',
                         'own_fund_type': '','approval_date':self.get_approval_date(), 'start_date': '', 'end_date': '',
                         'is_ministry_project':0,'sponsoring_ministry':'','planning_division':'','project_activity':'',
                          'project_benefit':'','project_purpose':''}
        project_name=''
        project_name_raw=''
        total_cost=''
        cost_unit=''
        gob_cost=''
        pa_cost=''
        own_fund=''
        ministry=''
        planning=''
        start_date=''
        end_date=''
        try:
            flag='none'
            for key,value in data_dict.items():
                if(not mmrules.start_re.search(value)==None):
                    flag='p_name'
                    continue
                elif (not mmrules.project_purpose_re.search(value) == None):
                    mo = mmrules.project_purpose_re.search(value)
                    start = mo.group(0)
                    start_idx = len(start) + 2
                    result_dict['project_purpose'] = value[start_idx:]
                elif (not mmrules.project_activity_re.search(value) == None):
                    mo = mmrules.project_activity_re.search(value)
                    start = mo.group(0)
                    start_idx = len(start) + 2
                    result_dict['project_activity'] = value[start_idx:]
                elif(not mmrules.planning_div_start_re.search(value)==None):
                    mo1=mmrules.planning_div_start_re.search(value)
                    mo2=mmrules.planning_div_end_re.search(value)
                    start_div=mo1.group(0)
                    end_div=mo2.group(0)
                    idx_s=value.find(start_div)+len(start_div)
                    idx_e=value.find(end_div)
                    result_dict['planning_division']=value[idx_s:idx_e]
                    continue
                elif(not dpprules.ministy_re.search(value)==None):
                    flag='m_name'
                    continue
                elif (not dpprules.agency_re.search(value) == None):
                    flag = 'a_name'
                    continue
                elif (not dpprules.estimated_cost_re.search(value) == None):
                    flag = 'cost'
                    if('(' in value):
                        idx1=value.find('(')
                        idx2=value.find(')')
                        result_dict['cost_unit']=value[idx1+1:idx2]
                    continue
                elif(not dpprules.total_re.search(value)==None):
                    flag='total'
                    continue
                elif (not dpprules.gob_cost_re.search(value) == None):
                    flag = 'gob'
                    continue
                elif (not dpprules.pa_cost_re.search(value) == None):
                    flag = 'pa'
                    continue
                elif (not dpprules.own_fund_re.search(value) == None):
                    flag = 'own'
                    continue
                elif (not dpprules.date_re.search(value) == None):
                    flag = 'date'
                    continue
                elif(not dpprules.start_date_re.search(value)==None):
                    flag='s_date'
                    continue
                elif (not dpprules.end_date_re.search(value) == None):
                    flag = 'e_date'
                    continue
                elif(flag=='p_name'):
                    result_dict['project_name']=value
                    result_dict['project_name_raw']=self.raw_data[key]
                elif(flag=='m_name'):
                    result_dict['sponsoring_ministry']=value
                elif (flag == 'a_name'):
                    result_dict['executing_agency'] = value
                elif(flag=='total' and not mmrules.amount_re.search(value)==None):
                    result_dict['project_cost']=value
                elif (flag == 'gob' and not mmrules.amount_re.search(value) == None):
                    result_dict['gob_cost'] = value
                elif (flag == 'pa' and not mmrules.amount_re.search(value) == None):
                    result_dict['pa_cost'] = value
                elif (flag == 'own' and not mmrules.amount_re.search(value) == None):
                    result_dict['own_fund'] = value
                elif (flag == 's_date' and not mmrules.year_re.search(value)==None):
                    result_dict['start_date'] = value
                elif (flag == 'e_date' and not mmrules.year_re.search(value)==None):
                    result_dict['end_date'] = value
                    flag=''

            pprint(result_dict)
            return result_dict
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())
            return result_dict
























