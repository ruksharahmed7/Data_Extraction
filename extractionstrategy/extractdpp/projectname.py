import dataExtraction.rulesfile.rules as rules
import traceback
import pandas as pd
import dataExtraction.extractionstrategy.commonfunction as commonfunction


def extract_project_title(operational_data):
    try:
        json_data=[]
        title_keyword = ''
        project_title = ''
        title_location_track = []
        total_cost_keyword = ''
        total_cost=''
        cost_location_track = []
        title_flag=0
        idx=0
        back_track=0
        dict_data={}
        result_dict={}
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        df3 = pd.DataFrame()
        df4 = pd.DataFrame()
        title_idx = 0


        for key,data in sorted(operational_data.items()):
            #print(data)
            back_track-=1
            if(back_track<=0):
                title_flag=0
            if (not (rules.project_name_re.search(data) == None) and rules.project_name_garbage_re.search(data)==None and title_flag==0):
                mo = rules.project_name_re.search(data)
                title_keyword = mo.group(0)
                if((':' in data or 'ঃ' in data) and len(data)>30):
                    strat=data.find(':')
                    project_title=data[strat+1:]
                    #print(data[end+1:])
                    title_location_track.append(key)
                    loc = commonfunction.find_location(title_location_track)
                    dict_data = {'Project_title_' + str(title_idx): pd.Series([title_keyword, project_title, loc],
                                                                                index=['key', 'title',
                                                                                       'location_index'])}
                    df1 = pd.DataFrame(dict_data)
                    title_idx += 1
                    dict_data.clear()

                    json_data.insert(idx, [title_keyword, project_title])
                    json_data[idx].extend(title_location_track)
                    result_dict['project_name']=project_title
                    idx+=1
                    title_location_track.clear()
                    title_flag=0
                elif('\t' in data and len(data)>30):
                    strat = data.find('t')
                    project_title = data[strat + 1:]
                    #print(data[end + 1:])
                    title_location_track.append(key)
                    loc = commonfunction.find_location(title_location_track)
                    dict_data = {'Project_title_' + str(title_idx): pd.Series([title_keyword, project_title, loc],
                                                                              index=['key', 'title',
                                                                                     'location_index'])}
                    df2 = pd.DataFrame(dict_data)
                    title_idx += 1
                    dict_data.clear()

                    json_data.insert(idx, [title_keyword, project_title])
                    json_data[idx].extend(title_location_track)
                    result_dict['project_name'] = project_title
                    idx += 1
                    title_location_track.clear()
                    title_flag = 0
                else:
                    #print(data[end+1:])
                    title_location_track.append(key)
                    back_track=4
                    title_flag=1
                    continue
            elif(not rules.ministy_re.search(data)==None):
                print(project_title)
                loc = commonfunction.find_location(title_location_track)
                dict_data = {'Project_title_' + str(title_idx): pd.Series([title_keyword, project_title, loc],
                                                                          index=['key', 'title',
                                                                                 'location_index'])}
                df4 = pd.DataFrame(dict_data)
                title_idx += 1
                dict_data.clear()

                json_data.insert(idx, [title_keyword, project_title])
                json_data[idx].extend(title_location_track)
                result_dict['project_name'] = project_title
                idx += 1
                title_flag = 0
                title_location_track.clear()
                title_flag=0
                back_track=0
            elif(title_flag==1 and len(data)>30):
                project_title=data
                #print(data[end+1:])
                title_location_track.append(key)
                title_flag=2
                continue
            elif(title_flag==2 and len(data)>30):
                project_title+=' : '+data
                #print(data[end+1:])
                title_location_track.append(key)
                #print(title_location_track)
                loc = commonfunction.find_location(title_location_track)
                dict_data = {'Project_title_' + str(title_idx): pd.Series([title_keyword, project_title, loc],
                                                                          index=['key', 'title',
                                                                                 'location_index'])}
                df3 = pd.DataFrame(dict_data)
                title_idx += 1
                dict_data.clear()

                json_data.insert(idx,[title_keyword,project_title])
                json_data[idx].extend(title_location_track)
                result_dict['project_name'] = project_title
                idx+=1
                title_flag=0
                title_location_track.clear()
                continue
            elif(title_flag==2 and len(data)<30):
                loc = commonfunction.find_location(title_location_track)
                dict_data = {'Project_title_' + str(title_idx): pd.Series([title_keyword, project_title, loc],
                                                                          index=['key', 'title',
                                                                                 'location_index'])}
                df4 = pd.DataFrame(dict_data)
                title_idx += 1
                dict_data.clear()

                json_data.insert(idx, [title_keyword, project_title])
                json_data[idx].extend(title_location_track)
                result_dict['project_name'] = project_title
                idx += 1
                title_flag = 0
                title_location_track.clear()
        result_df = pd.concat([df1, df2, df3, df4], axis=1, sort=False)
        p_name=result_dict['project_name']
        p_name_ban=''
        p_name_eng=''
        if(':' in p_name):
            idx=p_name.find(':')
            p_name_ban=p_name[:idx]
            p_name_eng=p_name[idx+1:]
            result_dict['project_name']=p_name_ban
            result_dict['project_name_eng']=p_name_eng

        return json_data,result_df,result_dict
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None,None,None



def extract_project_title_(operational_data):
    try:
        project_title = ''
        title_flag=0
        idx=0
        back_track=0
        result_dict={}
        title_idx = 0
        for key,data in sorted(operational_data.items()):
            print(data)
            back_track-=1
            if(back_track<=0):
                title_flag=0
            if (not (rules.project_name_re.search(data) == None) and rules.project_name_garbage_re.search(data)==None and title_flag==0):
                if((':' in data or 'ঃ' in data) and len(data)>30):
                    strat=data.find(':')
                    project_title=data[strat+1:]
                    #print(data[end+1:])
                    result_dict['project_name']=project_title
                    title_flag=0
                elif('\t' in data and len(data)>30):
                    strat = data.find('t')
                    project_title = data[strat + 1:]
                    result_dict['project_name'] = project_title
                    title_flag = 0
                else:
                    #print(data[end+1:])
                    back_track=4
                    title_flag=1
                    continue
            elif(not rules.ministy_re.search(data)==None):
                #print(project_title)
                result_dict['project_name'] = project_title
                title_flag=0
                back_track=0
            elif(title_flag==1 and len(data)>30):
                project_title=data
                #print(data[end+1:])
                title_flag=2
                continue
            elif(title_flag==2 and len(data)>30):
                project_title+=' : '+data
                result_dict['project_name'] = project_title
                title_flag=0
                continue
            elif(title_flag==2 and len(data)<30):
                result_dict['project_name'] = project_title
                title_flag = 0
        p_name=result_dict['project_name']
        p_name_ban=''
        p_name_eng=''
        if(':' in p_name):
            idx=p_name.find(':')
            p_name_ban=p_name[:idx]
            p_name_eng=p_name[idx+1:]
            result_dict['project_name']=p_name_ban
            result_dict['project_name_eng']=p_name_eng

        return result_dict
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None
