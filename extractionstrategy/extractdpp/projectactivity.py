import dataExtraction.rulesfile.rules as rules
import dataExtraction.datapreprocessing.processingdata as cleaningdata
import traceback

def extract_activity(operational_data):
    try:
        result={}
        activity=''
        flag=0
        for key,value in sorted(operational_data.items()):
            value_clean=cleaningdata.cleaning_data(value)
            #print(key,value_clean)
            if(not rules.activity_re.search(value_clean)==None and flag==0):
                flag=1
                continue
            elif(not rules.stop_activity_re.search(value_clean)==None and flag==1):
                flag=0
            elif(flag==1):
                activity+=value+'\n'
        result['project_activity'] = activity
        return result
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None
