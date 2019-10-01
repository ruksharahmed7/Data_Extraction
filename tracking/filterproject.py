import pandas as pd
import dataExtraction.datapreprocessing.processingdata as processingdata
import pandas as pd
import traceback
from pprint import pprint
import re
import config as configfile
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def filter_project(result_list,project_name,project_id):
    try:
        res_list=[]
        project_name = processingdata.cleaning_data(project_name)
        idx = 0
        all_projects = {}
        print(len(result_list))
        for result in result_list:
            # print(result)
            p_name = result.get("project_name")
            p_name_clean = processingdata.cleaning_data(p_name)
            all_projects[idx] = p_name_clean
            idx += 1
        #pprint(all_projects)
        ratio=[]
        for key,project in all_projects.items():
            print(project)
            #print(fuzz.ratio(project_name,project))
            ratio.append(fuzz.partial_ratio(project_name, project))
        indx = ratio.index(max(ratio))
        if(ratio[indx]>90):
            res = result_list[indx]
            res['project_id'] = project_id
            res_list.append(res)
            return res_list
        else:
            return None
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None


def filtering_project_name(result_list,project_name,project_id):
    try:
        print(project_id,project_name)
        project_name=processingdata.cleaning_data(project_name)
        idx=0
        all_projects={}
        print(len(result_list))
        for result in result_list:
            #print(result)
            p_name=result.get("project_name")
            p_name_clean=processingdata.cleaning_data(p_name)
            p_name_token_list=processingdata.tokenizer(p_name_clean)
            all_projects[idx]=p_name_token_list
            idx+=1
        pprint(all_projects)
        #pprint(df_matrix)
        #pprint(project_name_list)
       # pprint(project_id_list)
        #pprint(project_name_token_list)
        #df_matrix.project.str.get_dummies(sep=' ').reindex(columns=splited_project_name)
        #pprint(df_matrix)

        #countvec = CountVectorizer(vocabulary=splited_project_name)
     #   dfFinal = pd.DataFrame(countvec.fit_transform(df_matrix.project).toarray(), index=df_matrix.id, columns=countvec.get_feature_names())
        #pprint(dfFinal)
        tf_percentage=[]
        first_word_check_flag=0

        for key,project in all_projects.items():
            pprint(project)
            word_count=0
            if(not re.search(project[0],project_name)==None):
                first_word_check_flag=1
            for word in project:
                if(not re.search(word,project_name)==None):
                    print('match:',word)
                    word_count+=1
                    #word_count+=check_match(splited_project_name,word)
            tf_percentage.append((word_count/len(project))*100)
        print("percentage")
        pprint(tf_percentage)
        indx=tf_percentage.index(max(tf_percentage))
        #print(indx)
        res_list = []
        if(tf_percentage[indx]>configfile.Threshold['tfidf_percentage'] and first_word_check_flag):
            res=result_list[indx]
            res['project_id']=project_id
            res_list.append(res)
            return res_list
        else:
            return None
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None



def check_match(splited_project_name,word):
    for token in splited_project_name:
        if(token==word):
            return 1
    return 0