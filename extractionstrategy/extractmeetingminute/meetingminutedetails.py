import dataExtraction.rulesfile.meetingminuterules as mmrules
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

    def __init__(self,clusteded_data):
        pprint(clusteded_data)
        df = pd.DataFrame()
        for key,value in sorted(clusteded_data.items()):
            data_dict={}
            data_dict,list_formate_data=self.extract(value,key)
            #print(data_dict)
            df = pd.DataFrame(data_dict)
            self.result = pd.concat([self.result, df], axis=1, sort=False)
            # print(dict_data)
            #if str(list_formate_data['project_id'])==str(project_id):
            self.restul_list.append(list_formate_data)
            del df
        #pprint(self.result)

    def get_result(self):
        return self.result,self.restul_list

    def clear_result(self):
        self.restul_list.clear()


    def extract(self,data,key):
        data_dict={}
        list_formate_data={}
        project_id=''
        project_name=''
        total_cost=''
        gob_cost=''
        cost_unit=''
        pa_cost=''
        pa_fund_type=''
        own_fund=''
        own_fund_type=''

        start_date=''
        end_date=''
        confidence_level=1
        start=data.find('“')
        end=0
        #print(start)
        if(start==-1):
            start = data.find('"')
            end=data[start+1:].find('"')
            project_name = data[start + 1:end+1]
        else:
            end=data[start+1:].find('”')
            project_name=data[start+1:end+1]
        print(project_name)
        other_data=data[end+2:]
        tokenizer = TokenizeSentence('bengali')
        bengali_text_tokenize = tokenizer.tokenize(data[end+2:])
        #print(bengali_text_tokenize)
        flag=0
        for i in range(len(bengali_text_tokenize)):
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
        idx1=other_data.find('[')
        idx2=other_data.find(']')
        if(idx2==-1):
            idx2=other_data.find('প্রাক্কলিত')
        if(idx1>0 and idx2>0):
            gob_cost,pa_cost,pa_fund_type,own_fund,own_fund_type=self.other_cost(other_data[idx1+1:idx2])

        print(other_data)

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
        #print(date_data)
        start_date,end_date=self.date_extract(date_data)
        #project_id=tracking.get_project_id(project_name)
        #print(project_name,total_cost, cost_unit, gob_cost, pa_cost, pa_fund_type, own_fund, own_fund_type,start_date,end_date)
        if(gob_cost==''):
            gob_cost=total_cost
        list_formate_data = {'project_id':project_id,'project_name': project_name, 'project_cost': total_cost, 'cost_unit': cost_unit,
                     'gob_cost': gob_cost, 'pa_fund': pa_cost, 'pa_fund_name': pa_fund_type, 'own_fund': own_fund,
                     'own_fund_type': own_fund_type, 'start_date': start_date, 'end_date': end_date,
                     'confidence_level': confidence_level,'location_index':str(key)}
        # pprint(data_dict)

        data_dict = {'approved_project_' + str(project_id): pd.Series(
            [project_name, total_cost,cost_unit,gob_cost,pa_cost,pa_fund_type,own_fund,own_fund_type, start_date, end_date, confidence_level,
             str(key)],
            index=['project_name', 'total_project_cost','cost_unit','gob_cost', 'pa_fund','pa_fund_name','own_fund','own_fund_name','start_date', 'end_date', 'confidence_level',
                   'location_index'])}
        return data_dict,list_formate_data





    def date_extract(self,date_data):
        mo=mmrules.break_re.search(date_data)
        txt=mo.group(0)
        idx=date_data.find(txt)
        l=len(txt)
        start_date=date_data[:idx]
        end_date=date_data[idx+l:]
        return start_date,end_date

    def other_cost(self,str):
        #print(str)
        #idx=str.find('এবং')
        #str1=str[:idx]
        #str2=str[idx+3:]
        #mo1=mmrules.amount_re.search(str1)
        #mo2=mmrules.amount_re.search(str2)
        data=[]
        idx1=str.find(',')
        if(idx1!=-1):
            data.append(str[:idx1])
            str=str[idx1+1:]
        idx2 = str.find('এবং')
        data.append(str[:idx2])
        data.append(str[idx2+3:])
        #pprint(data)
        gob_cost=''
        pa_cost=''
        pa_fund_type=''
        own_fund=''
        own_fund_type=''
        for val in data:
            if(not (mmrules.gob_re.search(val)==None)):
                mo=mmrules.amount_re.search(val)
                gob_cost=mo.group(0)
            if(not (mmrules.pa_re.search(val)==None)):
                mo = mmrules.amount_re.search(val)
                pa_cost = mo.group(0)
                start = val.find('(')
                end = val.find(')')
                if(start!=-1 and end!=-1):
                    pa_fund_type = val[start + 1:end]
            if (not (mmrules.own_fund_re.search(val) == None)):
                mo = mmrules.amount_re.search(val)
                own_fund = mo.group(0)
                start=val.find('(')
                end=val.find(')')
                own_fund_type=val[start+1:end]
        return gob_cost,pa_cost,pa_fund_type,own_fund,own_fund_type
































