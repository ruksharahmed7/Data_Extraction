import dataExtraction.rulesfile.resultanalysisrules as rarules

def check_date(date_dict):
    if(rarules.date_re.match(date_dict['start_date']) and rarules.date_re.match(date_dict['end_date'])):
        return True
    else:
        return False

def check_org(data_dict):
    if(not rarules.ministry_re.search(data_dict['sponsoring_ministry'])==None and len(data_dict['sponsoring_ministry'])>20):
        return True
    else:
        return False