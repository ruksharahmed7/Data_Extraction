import pandas as pd
import pprint
import re

main_part_re=re.compile(r'Part\s*A')

def readExcel(file_name):
    xl_file = pd.ExcelFile(file_name)
    dfs = {sheet_name: xl_file.parse(sheet_name)
           for sheet_name in xl_file.sheet_names}
    #print(dfs['Part A (1-8)'])
    for key,value in dfs.items():
        if(not main_part_re.search(key)==None):
            df=dfs[key]
            print(df.ix(0))
