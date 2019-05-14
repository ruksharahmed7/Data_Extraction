import dataExtraction.rulesfile.rules as rules
import traceback
import pandas as pd
import dataExtraction.extractionstrategy.commonfunction as commonfunction
from pprint import pprint


def extract_purpose(operational_data):
    try:
        result_dict={}
        objective=''
        flag=0
        for key,value in sorted(operational_data.items()):
            #print(key,value)
            if(not rules.objective_re.search(value)==None and flag==0):
                flag=1
                print('f')
                continue
            elif(not rules.escape_objective_re.search(value)==None):
                #print('ex')
                continue
            elif(not (rules.date_re.search(value)==None)):
                flag=0
                #print("h")
            elif(not (rules.stop_objective_re.search(value)==None)):
                flag=0
            elif(flag==1):
                #print('s')
                objective+=value
        #print(objective)
        result_dict['project_purpose']=objective
        #pprint(result_dict)
        return result_dict
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None