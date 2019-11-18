import traceback
from pprint import pprint

from fuzzywuzzy import fuzz


def map(result_dict):
    try:
        ministry_idx=-1
        division_idx=-1
        #print(result_dict['sponsoring_ministry'])
        ministry_division=result_dict['sponsoring_ministry']
        f = open("dataExtraction/masterdata/ministry.txt")
        ministries = f.readlines()
        f = open("dataExtraction/masterdata/division.txt")
        divisions=f.readlines()

        #pprint(lines)
        ministry_ratio=[]
        division_ratio=[]
        for i in range(len(ministries)):
            ministry_ratio.append(fuzz.partial_ratio(ministry_division, ministries[i]))
            #print(ministries[i],ministry_ratio[i])
        #print('division matching')
        for i in range(len(divisions)):
            division_ratio.append(fuzz.partial_ratio(ministry_division, divisions[i]))
            #print(divisions[i],division_ratio[i])
        ministry_idx = ministry_ratio.index(max(ministry_ratio))
        division_idx = division_ratio.index(max(division_ratio))
        result_dict['sponsoring_ministry_map']=ministry_idx+1
        result_dict['cabinet_division_map']=division_idx+1
        return [result_dict]
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        result_dict['sponsoring_ministry_map'] = ministry_idx + 1
        result_dict['cabinet_division_map'] = division_idx + 1
        return [result_dict]