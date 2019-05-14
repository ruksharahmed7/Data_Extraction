import numpy as np
import dataExtraction.rulesfile.clusteringrules as rules

def labeling(train_clean_sentences):
    n=len(train_clean_sentences)
    print(n)
    y_train=np.zeros(n)
    #pprint(y_train[1])
    idx=-1
    flag=0
    for val in train_clean_sentences:
        idx+=1
        if(not (rules.project_name_re.search(val)==None)):
            y_train[idx]=1
            flag=1
            continue
        if(not (rules.ministry_re.search(val)==None)):
            y_train[idx] = 2
            flag = 2
            continue
        if (not (rules.agency_re.search(val) == None)):
            y_train[idx] = 2
            flag = 2
            continue
        if (not (rules.planning_division_re.search(val) == None)):
            y_train[idx] = 2
            flag = 2
            continue
        if (not (rules.point_re.search(val) == None) and flag!=0):
            print('here',flag)
            flag = 0
        if (flag == 1):
            y_train[idx] = 1
        if(flag==2):
            y_train[idx] = 2
    return y_train