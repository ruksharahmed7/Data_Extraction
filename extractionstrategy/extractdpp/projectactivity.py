import dataExtraction.rulesfile.rules as rules
import traceback

def extract_activity(operational_data):
    try:
        result={}
        result['project_activity']='actively activated'
        return result
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None
