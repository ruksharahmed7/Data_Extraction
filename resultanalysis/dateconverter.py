import dataExtraction.rulesfile.convertingrules as rules
from .stmconverter import digit_convert as digitconverter
from .stmconverter import month_convert as monthconverter
import traceback
def converter(date):
    try:
        print('data converting:',date)
        if(not rules.date_formate_1_re.search(date)==None):
            print('format 1')
            dates=[]
            if('.' in date):
                dates=date.split('.')
            if ('-' in date):
                dates = date.split('-')
            if ('/' in date):
                dates = date.split('/')
            month=digitconverter(dates[1])
            year=digitconverter(dates[2])
            print(month,year)
            return month,year

        elif(not rules.year_formate_re.search(date)==None):
            print('format 2')
            mo=rules.year_formate_re.search(date)
            year_raw=mo.group(0)
            year=digitconverter(year_raw)
            month=monthconverter(date)
            print(month,year)
            return month,year

        else:
            print(date)
            return None,None

    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None,None