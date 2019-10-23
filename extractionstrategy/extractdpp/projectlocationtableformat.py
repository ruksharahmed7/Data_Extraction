import dataExtraction.rulesfile.locationrules as rules

def verify_location_keys(keys):
    #print(keys)
    div_flag=False
    dis_flag=False
    up_flag=False
    count=0
    for key in keys:
        if (not rules.upazila_re.search(key) == None):
            up_flag = True
            count+=1
        elif(not rules.district_re.search(key)==None):
            dis_flag=True
            count+=1
        elif(not rules.division_re.search(key)==None):
            div_flag=True
            count+=1
    #print(div_flag,dis_flag,up_flag)
    if(div_flag and dis_flag and up_flag and (len(keys)<5 or len(keys)==count)):
        print('matched')
        return True
    else:
        return False

def convert_location(data):
    location_list=[]
    for dict in data:
        location={}
        for key,value in dict.items():
            if (not rules.upazila_re.search(key) == None):
                location['upzila']=value
            elif (not rules.district_re.search(key) == None):
                location['district'] = value
            elif (not rules.division_re.search(key) == None):
                location['division']=value
        location_list.append(location)
    return location_list