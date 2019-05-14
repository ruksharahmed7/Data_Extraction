import pandas as pd
import dataExtraction.datapreprocessing.processingdata as processingdata
import pandas as pd
import traceback
from pprint import pprint
import re

def set_project_id(project_id,project_name):
    cleaned_project_name=processingdata.cleaning_data(project_name)
    #print(project_name,cleaned_project_name)
    #project_track_dict = {'Tracking project': pd.Series(
     #   [project_id,project_name, cleaned_project_name],
      #  index=['project_id','project_name', 'cleaned_project_name'])}

    project_track_dict = {'project_id':[project_id],'project_name':[project_name],'clean_project_name':[cleaned_project_name]}
    df = pd.DataFrame(project_track_dict,index=[project_id])
    track_list=[project_id,project_name,cleaned_project_name]

    with open('project_track.csv', 'a') as f:
        df.to_csv(f, header=False)

    project_track_dict.clear()
    data = pd.read_csv("project_track.csv")
    #pprint(data)
    del df

def get_project_id(project_name):
    try:
        project_id = ''
        project_name=processingdata.cleaning_data(project_name)
        #print('project_name:')
        #print(project_name)
        #print(project_name)
        splited_project_name=project_name.split(' ')
        #print(splited_project_name)


        data = pd.read_csv("project_track.csv", header=None, usecols=[1,2,3])

        project_name_list=data[3].tolist()
        project_id_list=data[1].tolist()
        df_matrix_1=pd.DataFrame(project_name_list,index=None,columns=['project'])
        df_matrix_2=pd.DataFrame(project_id_list,index=None,columns=['id'])
        df_matrix = pd.concat([df_matrix_1,df_matrix_2], axis=1, sort=False)
        #pprint(df_matrix)
        #pprint(project_name_list)
       # pprint(project_id_list)
        project_name_token_list=[]
        for value in project_name_list:
            project_name_token=processingdata.tokenizer(value)
            project_name_token_list.append(project_name_token)
        #pprint(project_name_token_list)
        #df_matrix.project.str.get_dummies(sep=' ').reindex(columns=splited_project_name)
        #pprint(df_matrix)

        #countvec = CountVectorizer(vocabulary=splited_project_name)
     #   dfFinal = pd.DataFrame(countvec.fit_transform(df_matrix.project).toarray(), index=df_matrix.id, columns=countvec.get_feature_names())
        #pprint(dfFinal)
        tf_percentage=[]
        first_word_check_flag=0

        for project in project_name_token_list:
            #pprint(project)
            word_count=0
            if(not re.search(project[0],project_name)==None):
                first_word_check_flag=1
            for word in project:
                if(not re.search(word,project_name)==None):
                    #print('match:',word)
                    word_count+=1
                    #word_count+=check_match(splited_project_name,word)
            tf_percentage.append((word_count/len(project))*100)
        #pprint(tf_percentage)
        indx=tf_percentage.index(max(tf_percentage))
        #print(indx)

        if(tf_percentage[indx]>60.0 and first_word_check_flag):
            project_id=project_id_list[indx]
            #print('matched with:')
            #print(project_id)
            #print(project_name_list[indx])

        return project_id
    except Exception as e:
        return ""



def check_match(splited_project_name,word):
    for token in splited_project_name:
        if(token==word):
            return 1
    return 0
