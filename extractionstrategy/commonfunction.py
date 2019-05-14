def find_index(data):
    if(':' in data):
        return data.find(':')
    elif('t' in data):
        return data.find('t')
    else:
        return data.find('ঃ')

def find_location(location_arr):
    loc=''
    for itm in location_arr:
        loc=loc+str(itm)+','
    return loc