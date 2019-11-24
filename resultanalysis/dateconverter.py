import dataExtraction.rulesfile.convertingrules as rules
from .stmconverter import digit_convert as digitconverter
from .stmconverter import month_convert as monthconverter
from .stmconverter import date_digit_convert as dateconverter
from .stmconverter import month_to_mm
import traceback
def date_converter(date):
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
            m=digitconverter(dates[1])
            month=monthconverter(m)
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

def date_convert_1(date):
    try:
        print(date)
        if(date.find('(')):
            idx=date.find('(')
            date=date[:idx]
            print(date)
        if(not rules.day_re.search(date)==None):
            mo1=rules.day_re.search(date)
            day=mo1.group(0)
            day=digitconverter(day)
            if(len(day)==1):
                day='0'+day
            print(day)
        if(not rules.year_formate_re.search(date)==None):
            mo2 = rules.year_formate_re.search(date)
            year = mo2.group(0)
            year = digitconverter(year)
        month=monthconverter(date)
        month=month_to_mm(month)
        print(month,year)
        return day+'-'+month+'-'+year
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return date

def approval_date_convert(date):
    print("converting approval date",date)
    d=dateconverter(date)
    d=date_fit(d)
    print('approvalDate:',d)
    if(not rules.date_formate_goal.match(d)):
        d=date_convert_1(date)
        return d
    return d

def date_fit(Date):
    try:
        date=Date.split('-')
        print(date)
        if(not len(date[0])==2):
            date[0]='0'+date[0]
        if (not len(date[1]) == 2):
            date[1] = '0' + date[1]
        if (not len(date[2]) == 4):
            date[2] = '20' + date[2]
        return date[0]+'-'+date[1]+'-'+date[2]
    except:
        return Date





