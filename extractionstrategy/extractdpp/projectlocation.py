import dataExtraction.rulesfile.rules as rules
import traceback
import pandas as pd
import dataExtraction.extractionstrategy.commonfunction as commonfunction
import dataExtraction.datapreprocessing.processingdata as processing
from pprint import pprint

def extract_location(operational_data):
    try:
        geo_location=[]
        result_dict={}
        flag=0
        for key,value in sorted(operational_data.items()):
            clean_value=processing.cleaning_data(value)
            #print(clean_value)
            if(not rules.geo_re.search(value)==None and flag==0 and len(value)<80 and rules.not_geo_re.search(value)==None):
                flag=1
                print('got', value)
            elif(flag==1 and (not rules.estimated_cost_re.search(value)==None or not rules.stop_geo_re.search(value)==None)):
                flag=0
            elif(flag==1 and len(value)>150):
                geo_location.clear()
                flag=0
                continue
            elif(flag==1):
                print(value)
                geo_location.append(value)
        result_dict['project_location']=geo_location
        #pprint(result_dict)
        return result_dict
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None

