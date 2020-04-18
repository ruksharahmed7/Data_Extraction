# -*- coding: utf-8 -*-
#happy_coding('~')
import json
import traceback

import dataExtraction.filereader.docreader as docreader
import dataExtraction.getmetadata.mergedata as mergedata
from dataExtraction.fileconveter.docxtopdf import convert_to
from dataExtraction.projectlinking.parentproject import get_parent_project

import os
from flask import Flask, jsonify, request, flash, render_template
####APP configuration#####
#Start#
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
ROOT_DIR = os.path.abspath("../../")
#pathToLibrary = 'C:/Users/BR450s8g180h/Documents/backend/library'
pathToLibrary = '/home/raihan/library'

TTFSearchPath = (
            'c:/winnt/fonts',
            'c:/windows/fonts',
            '/usr/lib/X11/fonts/TrueType/',
            '/usr/share/fonts/truetype',
            '/usr/share/fonts',             #Linux, Fedora
            '/usr/share/fonts/dejav',      #Linux, Fedora
            '%(REPORTLAB_DIR)s/fonts',      #special
            '%(REPORTLAB_DIR)s/../fonts',   #special
            '%(REPORTLAB_DIR)s/../../fonts',#special
            '%(CWD)s/fonts',                #special
            '~/fonts',
            '~/.fonts',
            '%(XDG_DATA_HOME)s/fonts',
            '~/.local/share/fonts',
            #mac os X - from
            #http://developer.apple.com/technotes/tn/tn2024.html
            '~/Library/Fonts',
            '/Library/Fonts',
            '/Network/Library/Fonts',
            '/System/Library/Fonts',
            )

#End#

"""
 Data extraction API. Method POST,
 Input field "project_name,project_id,folder_name,file_name".
 Call get_tasks function where the internal all functions and method will be called.
 This API Return result(a list of dictionary) in json format.
"""
@app.route('/data_extraction',methods=['POST'])
def extraction_():
    try:
        data=request.get_json(force=True)
        project_name = data['project_name']
        project_id = data['project_id']
        folder_name = data['folder_name']
        file_name = data['file_name']
        print(project_name)
        return get_tasks(folder_name, file_name, str(project_id), project_name)
    except Exception as e:
        return '<p>error<p>'

"""
Project Linking API. input project_name and get parent_project name
"""
@app.route('/project_link',methods=['POST'])
def linking():
    try:
        data = request.get_json(force=True)
        project_name=data['project_name']
        project_list=get_parent_project(project_name)  ### Fuzzy String Compare. input project name with existing projects
        return jsonify(project_list)  ##return a json list. Al possible parent project_name exceded threshold ratio
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return jsonify([{'response': 'error'}])


"""
This api convert docx file to pdf file
"""
@app.route('/file_convert',methods=['POST'])
def conversion():
    try:
        data = request.get_json(force=True)
        folder_name=data['folder_name']
        file_name=data['file_name']
        directory = pathToLibrary
        foldername=directory+folder_name+'/'
        filename=foldername+file_name
        check_exist_file=filename + '.pdf'
        if os.path.isfile(check_exist_file):
            return jsonify([{'response':'Already coverted'}])
        converted_file_name = convert_to(foldername, filename) ##conversion function. Subporcess method
        print(converted_file_name)
        os.rename(converted_file_name, check_exist_file)
        return jsonify([{'response': 'Successfully converted to PDF'}])
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return jsonify([{'response': 'error'}])


#####Data Extraction API call this function#####
def get_tasks(folder_name,file_name,project_id,project_name):
    file_location=pathToLibrary+'/'+ folder_name +'/'+ file_name
    ### data reading from doc file. Return dictionary
    data_list, raw_data, converted_data = docreader.doc_reader_tree_formate(file_location)
    if(folder_name=='dpp'):
        dpp_result=mergedata.clustering_and_get_merge_dpp(raw_data, converted_data,project_id) ##DPP Operation
        #pprint(dpp_result)
        ### Location data in tab format ###
        location_data = docreader.getTableData(file_location)
        dpp_result_final=mergedata.merge_location(dpp_result,location_data)
        finalresult = json.loads(dpp_result_final)
    if(folder_name=='summary'):
        summary_result=mergedata.get_merge_summary(raw_data, converted_data,project_id,project_name) ##Summary operation
        finalresult = json.loads(summary_result)
    if (folder_name == 'meetingminute'):
        password='ecnec14'
        meetingminute_result = mergedata.get_merge_meetingminute(raw_data, converted_data,project_id,project_name) ##MeetingMinute Operation
        finalresult = json.loads(meetingminute_result)
    return jsonify(finalresult)

if __name__ == '__main__':
    app.run(host='localhost',port='5555') ###Change Host and Port as your server




