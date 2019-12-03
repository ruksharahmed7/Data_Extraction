import requests
import re
from fuzzywuzzy import fuzz
from config import Threshold

first_rivision=re.compile(r'১ম\s*সংশোধিত')
second_rivision=re.compile(r'২য়\s*সংশোধিত')
third_rivision=re.compile(r'৩য়\s*সংশোধিত')

class APIError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)


def get_parent_project(project_name):
    try:
        resp = requests.get('http://120.50.8.205:2942/api/main/getAllProjectName')
        print(project_name)
        print(Threshold['project_linking_score'])
        project_list=[]
        result=[]
        ratio_list=[]
        for todo_item in resp.json():
            ratio=fuzz.partial_ratio(project_name, todo_item['projectname'])
            if(ratio>Threshold['project_linking_score'] and ratio!=100):
                print('{} {}'.format(todo_item['id'], todo_item['projectname']),ratio)
                ratio_list.append(ratio)
                project_list.append(todo_item)
        # if(not first_rivision.search(project_name)==None and len(project_list)!=0):
        #     print(ratio_list)
        #     indx = ratio_list.index(max(ratio_list))
        #     result.append(project_list[indx])
        return project_list

    except APIError as error:
        print(error)
