import dataExtraction.rulesfile.rules as rules
import traceback
import pandas as pd
import dataExtraction.extractionstrategy.commonfunction as commonfunction


def extract_date_1(operational_data):
    try:
        json_data=[]
        dict_data={}
        result_dict={}
        date_key= ''
        date_key_track=''
        start_date_key=''
        end_date_key=''
        start_date=''
        end_date=''
        date_location_track = []
        date_flag=0
        idx=0
        back_track=0
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        df3 = pd.DataFrame()
        df4 = pd.DataFrame()
        start_date_idx = 0
        end_date_idx=0
        for key,data in sorted(operational_data.items()):
            #print(data)
            back_track-=1
            if(back_track<=0):
                date_flag=0
                date_location_track.clear()
            if (not (rules.date_re.search(data) == None) and date_flag==0):
                mo = rules.date_re.search(data)
                date_key = mo.group(0)
                #print(date_key)
                date_location_track.append(key)
                date_key_track=data
                date_flag=1
                back_track=10
            elif(not (rules.start_date_re.search(data) == None) and date_flag==1):
                mo = rules.start_date_re.search(data)
                start_date_key = mo.group(0)
                print(start_date_key)
                date_location_track.append(data)
                if ((':' in data or 't' in data or 'ঃ' in data) and len(data)>30):
                    track = commonfunction.find_index(data)
                    start_date = data[track+1:]
                    loc=commonfunction.find_location(date_location_track)
                    dict_data={'Start_date_'+str(start_date_idx):  pd.Series([date_key, start_date_key, start_date,loc], index=['key', 'date_type', 'date','location_index'])}
                    df1=pd.DataFrame(dict_data)
                    start_date_idx+=1
                    dict_data.clear()
                    #print(df)
                    json_data.insert(idx, [date_key, start_date_key, start_date])
                    json_data[idx].extend(date_location_track)
                    result_dict['start_date']=start_date
                    idx += 1
                    date_flag = 3
                    back_track -= 2
                else:
                    date_flag=2
                    back_track-=1
            elif(date_flag==2 and not (rules.date_format_re.search(data)==None)):
                start_date=data
                date_location_track.append(data)
                loc = commonfunction.find_location(date_location_track)
                dict_data = {'Start_date_'+str(start_date_idx): pd.Series([date_key, start_date_key, start_date,loc], index=['key', 'date_type', 'date','location_index'])}
                df2 = pd.DataFrame(dict_data)
                start_date_idx+=1
                dict_data.clear()
                #print(df)
                json_data.insert(idx, [date_key, start_date_key, start_date])
                json_data[idx].extend(date_location_track)
                idx+=1
                date_flag = 3
                back_track-=1
                date_location_track.clear()
                result_dict['start_date']=start_date
            elif(not (rules.end_date_re.search(data) == None) and date_flag==3):
                mo = rules.end_date_re.search(data)
                end_date_key = mo.group(0)
                print(end_date_key)
                date_location_track.append(data)
                if ((':' in data or 't' in data or 'ঃ' in data) and len(data)>25):
                    track = commonfunction.find_index(data);
                    end_date = data[track+1:]
                    loc = commonfunction.find_location(date_location_track)
                    dict_data = {'End_date_'+str(end_date_idx): pd.Series([date_key, end_date_key, end_date, loc],
                                                         index=['key', 'date_type', 'date', 'location_index'])}
                    df3 = pd.DataFrame(dict_data)
                    end_date_idx+=1
                    dict_data.clear()
                    #print(df3)
                    #df.append(df3,sort=False,ignore_index = True)
                    json_data.insert(idx, [date_key, end_date_key, end_date])
                    json_data[idx].extend(date_location_track)
                    result_dict['end_date']=end_date
                    date_location_track.clear()
                    date_flag = 0
                    back_track -= 2
                else:
                    date_flag=4
                    back_track-=1
                    continue
            elif(date_flag==4 and not (rules.date_format_re.search(data)==None)):
                end_date = data
                print(end_date)
                date_location_track.append(data)
                loc = commonfunction.find_location(date_location_track)
                dict_data = {'End_date_'+str(end_date_idx): pd.Series([date_key, end_date_key, end_date, loc],
                                                   index=['key', 'date_type', 'date', 'location_index'])}
                df4 = pd.DataFrame(dict_data)
                end_date_idx+=1
                dict_data.clear()
                #print(df4)
                #df.append(df4,sort=False,ignore_index = True)
                json_data.insert(idx, [date_key, end_date_key, end_date])
                json_data[idx].extend(date_location_track)
                result_dict['end_date'] = end_date
                idx += 1
                date_flag = 0
                back_track -= 1
                date_location_track.clear()
        result_df = pd.concat([df1,df2,df3, df4], axis=1, sort=False)
        #print(result)
        del df1,df2,df3,df4
        return result_df,result_dict
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None,None

def extract_date_2(operational_data):
    try:
        json_data=[]
        dict_data={}
        result_dict={}
        date_type=[]
        date_key= ''
        date_key_track=0
        start_date_key=''
        start_date_track=0
        end_date_track=0
        end_date_key=''
        start_date=''
        end_date=''
        date_location_track = []
        date_flag=0
        idx=0
        start_date_idx=0
        end_date_idx=0
        back_track=0
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        control_flag=0
        for key,data in sorted(operational_data.items()):
            #print(key,data)
            control_flag+=1
            back_track -= 1
            if (back_track <= 0):
                date_flag = 0
                date_location_track.clear()
            if (not (rules.date_re.search(data) == None) and date_flag==0):
                mo = rules.date_re.search(data)
                date_key = mo.group(0)
                #print(date_key)
                date_location_track.append(key)
                date_key_track=key
                date_flag=1
                back_track=8

            elif (not (rules.start_date_re.search(data) == None) and date_flag == 1):
                mo = rules.start_date_re.search(data)
                start_date_key = mo.group(0)
                #print(start_date_key)
                start_date_track=key
                date_flag=2
                back_track-=1
                control_flag = 0

            elif (not (rules.end_date_re.search(data) == None) and date_flag == 2 and control_flag<2):
                mo = rules.end_date_re.search(data)
                end_date_key = mo.group(0)
                #print(end_date_key)
                end_date_track=key
                date_flag = 3
                back_track -= 1
            elif(date_flag==3):
                start_date=data
                #print(start_date)
                dict_data = {'start_date_'+str(start_date_idx) : pd.Series([date_key, start_date_key, start_date,str(date_key_track)+','+str(start_date_track)+','+str(key)],
                                                                        index=['key', 'date_type', 'date','location_index'])}
                #print(dict_data)
                df1 = pd.DataFrame(dict_data)
                result_dict['start_date']=start_date
                start_date_idx+=1
                #print(df1)
                dict_data.clear()
                date_flag=4
                back_track-=1
            elif(date_flag==4):
                end_date=data
                dict_data = {'end_date_'+str(end_date_idx): pd.Series([date_key, end_date_key, end_date,str(date_key_track)+','+str(end_date_track)+','+str(key)],
                                                     index=['key', 'date_type', 'date','location_index'])}
                df2 = pd.DataFrame(dict_data)
                result_dict['end_date'] = end_date
                end_date_idx+=1
                dict_data.clear()
                date_flag = 0
                back_track -= 1
        result_df = pd.concat([df1, df2], axis=1, sort=False)
        #print(result)
        del df1, df2
        return result_df,result_dict
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None,None

def extract_date_3(operational_data):
    try:
        print('extract strategy 3')
        flag=0
        data_dict={}
        back_track=20
        for key,value in sorted(operational_data.items()):
            #print(value)
            if(flag!=0):
                back_track-=1
            if(back_track<0):
                flag=0
            if(not rules.date_re.search(value)==None and flag==0):
                print(key,value)
                flag=1
            elif(flag==1 and not rules.start_date_re.search(value)==None):
                flag=10
            elif(flag==10 and not rules.end_date_re.search(value)==None):
                flag=11
            elif(not rules.original_date_re.search(value)==None and flag==11 and back_track>0):
                print(key,value)
                flag=2
            elif(not rules.revised_date_re.search(value)==None and flag==11 and back_track>0):
                print(key,value)
                flag=3
            elif(flag==2 and not rules.date_format_re.search(value)==None and back_track>0):
                print(key,value)
                data_dict['start_date']=value
                flag=4
                continue
            elif (flag == 4 and not rules.date_format_re.search(value)==None and back_track>0):
                print('end')
                print(key,value)
                data_dict['end_date'] = value
                flag=11
            elif (flag == 3 and not rules.date_format_re.search(value)==None and back_track>0):
                print(key,value)
                data_dict['revised_start_date'] = value
                flag=5
                continue
            elif (flag == 5 and not rules.date_format_re.search(value)==None and back_track>0):
                print('rev end')
                data_dict['revised_end_date'] = value
                break
        print(data_dict)
        return data_dict
    except Exception as e:
        data_dict['start_date']=''
        data_dict['end_date']=''
        data_dict['revised_start_date']=''
        data_dict['revised_end_date']=''
        return data_dict


def extract_date_exception(operational_data):
    try:
        #print(operational_data)
        data_dict={}
        flag=0
        for key,value in sorted(operational_data.items()):
            if(not rules.date_re.search(value)==None):
                flag=1
            elif(flag==1 and not rules.mid_point_re.search(value)==None):
                print(value)
                mo=rules.year_re.search(value)
                start_year=mo.group(0)
                indx=value.find(start_year)
                start_date=value[:indx+len(start_year)]
                moo=rules.mid_point_re.search(value)
                mid_point=moo.group(0)
                start_idx=value.find(mid_point)+len(mid_point)
                mo = rules.year_re.search(value[indx+len(start_year):])
                end_year=mo.group(0)
                end_idx=value.find(end_year)+len(end_year)
                end_date=value[start_idx:end_idx]
                data_dict['start_date']=start_date
                data_dict['end_date']=end_date
                flag=0
        print(data_dict)
        return data_dict
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return None