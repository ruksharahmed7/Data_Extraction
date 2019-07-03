import dataExtraction.rulesfile.convertingrules as rules
from .stmconverter import digit_convert as digitconverter
import math
import traceback
def convert(cost,unit):
    try:
        print(cost,unit)
        #print(cost)
        if(not rules.number_re.search(cost)==None):
            mo=rules.number_re.search(cost)
            cost=mo.group(0)
            cost = digitconverter(cost)
            print(float(cost))
            if(not rules.lakh_re.search(unit)==None):
                cost=float(cost)*1.0
            elif (not rules.core_re.search(unit) == None):
                cost=float(cost) * 100.0
        print(cost)
        return cost
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None




