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
            if(not rules.geo_re.search(clean_value)==None and flag==0 and len(clean_value)<50):
                flag=1
            if(not rules.estimated_cost_re.search(value)==None):
                flag=0
            if(flag==1):
                geo_location.append(value)
        result_dict['project_location']=geo_location
        #pprint(result_dict)
        return result_dict
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None

