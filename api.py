# -*- coding: utf-8 -*-
#happy_coding('~')
import json
import dataExtraction.filereader.docreader as docreader
import dataExtraction.filereader.readpdf as readpdf
import dataExtraction.getmetadata.mergedata as mergedata
import dataExtraction.tracking.trackingprojectid as tracking
import dataExtraction.tracking.trackingdb as trackingfromdb
from pprint import pprint
import dataExtraction.fileconveter.doctodocx as doctodocx
import glob
import subprocess

import os
import dataExtraction.database.connectdb as db

#print('Here:'+font.__str__('cjøx Dbœqb I mgevq gš¿Yvjq/¯’vbxq miKvi wefvM'))

from flask import Flask, jsonify, request, flash, render_template
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

ROOT_DIR = os.path.abspath("../../")


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

pdf_file_name = 'dataExtraction/dppFile/pdf/dpp1.pdf'

# For debugging
# Begin
#pdftotext.extract(pdf_file_name)
#text=pdfreader.extract_pdf(pdf_file_name)
#text=pyreader.convert_pdf_to_html(pdf_file_name)
#text=readpdf.pdf_to_text(pdf_file_name)
#print(text)


#meetingMinute
#data_list,raw_data,converted_data=docreader.doc_reader_tree_formate('dataExtraction/dppFile/meetingminute/mm2.docx')
#pprint(raw_data)
#mergedata.get_merge_meetingminute(raw_data,converted_data)


#~ data_list="xy!› öœ"
#data_list,raw_data,converted_data=docreader.doc_reader_tree_formate('dataExtraction/dppFile/doc/newdpp2.docx')
#test_data_list,test_raw_data,test_converted_data=docreader.doc_reader_tree_formate('dataExtraction/dppFile/doc/newdpp2.docx')

#mergedata.get_merge_dpp_1(data_list, converted_data,test_converted_data)
#finalresult = json.loads(dpp_result)
#print(finalresult)
#raw_data=docreader.get_docx_text('dataExtraction/dppFile/dppsummary/Summary01.docx')
#print(data_list)
#pprint(converted_data)
#result=mergedata.get_summary_merge_data(raw_data,converted_data)
#print(result)
#print(raw_data[0])
#docreader.print_doc('dataExtraction/dppFile/dppsummary/Summary01.docx')

# End


file='/home/babl/DDAS/library/dppFile/doc/dpp4.docx'
if('.docx' not in file):
    root = "/home/babl/DDAS/library/dppFile/"
    data_path = root + '/doc/'
    os.chdir(data_path)
    for doc in glob.iglob("*.doc"):
        print(doc)
        subprocess.call(['soffice', '--headless', '--convert-to', 'docx', doc], shell=True)
        #doctodocx.doc_to_docx_converting(file)
    #for doc in glob.iglob("*.doc"):
        #subprocess.call(['soffice', '--headless', '--convert-to', 'docx', doc])
    idx=file.find('.')
    file=file[:idx]+'.docx'
    print(file)

data_list,raw_data,converted_data =docreader.doc_reader_tree_formate(file)
#pprint(raw_data)
dpp_result=mergedata.clustering_and_get_merge_dpp(raw_data, converted_data,'12345')
#pprint(dpp_result)
#finalresult = json.loads(dpp_result)
#print(finalresult)

#@app.route('/<string:folder_name>/<string:dpp_name>', methods=['POST','GET'])
@app.route('/',methods=['POST'])
def start():
    Test=request.form['test']
    print(Test)


@app.route('/extraction',methods=['POST'])
def extraction_():
    try:
        db.create()
        print('Hit')
        data=request.get_json(force=True)
        project_name = data['project_name']
        project_id = data['project_id']
        folder_name = data['folder_name']
        file_name = data['file_name']
        print(project_name)
        p_name = trackingfromdb.get_project_name(str(project_id))
        print(p_name)
        if p_name == "" or p_name == None:
            trackingfromdb.insertnewproject(str(project_id), project_name)
            return get_tasks(folder_name, file_name, str(project_id),project_name)
        else:
            print('id matched', p_name)
            return get_tasks(folder_name, file_name, str(project_id),project_name)
    except Exception as e:
        return '<p>error<p>'


@app.route('/data_extraction',methods=['POST'])
def extraction():
    try:
        data=request.get_json(force=True)
        project_name = data['project_name']
        project_id = data['project_id']
        folder_name = data['folder_name']
        file_name = data['file_name']
        print(project_name)
        p_id = tracking.get_project_id(project_name)
        print(p_id)
        if str(p_id) == str(project_id):
            print('id matched', project_id)
            return get_tasks(folder_name, file_name, str(project_id))
        elif str(p_id) == "" or p_id == None:
            tracking.set_project_id(str(project_id), project_name)
            return get_tasks(folder_name, file_name, str(project_id))
    except Exception as e:
        return '<p>error<p>'

def get_tasks(folder_name,file_name,project_id,project_name):
    print("inside get_task")
    #object_list = getTableData('dppFile/doc/'+dpp_name)
    #print(object_list)
    file_location='/home/babl/DDAS/library/dppFile/'+ folder_name +'/'+ file_name
    data_list,raw_data,converted_data =docreader.doc_reader_tree_formate(file_location)
    #pprint(raw_data)
    if(folder_name=='dpp'):
        #db.update_dpp_status()
        dpp_result=mergedata.clustering_and_get_merge_dpp(raw_data, converted_data,project_id)
        finalresult = json.loads(dpp_result)
    if(folder_name=='summary'):
        summary_result=mergedata.get_merge_summary(raw_data, converted_data,project_id,project_name)
        finalresult = json.loads(summary_result)
    if (folder_name == 'meetingminute'):
        meetingminute_result = mergedata.get_merge_meetingminute(raw_data, converted_data,project_id,project_name)
        finalresult = json.loads(meetingminute_result)
    return jsonify(finalresult)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5555')




