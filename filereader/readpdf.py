from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
from pprint import pprint
import io
import os

from bijoy2unicode import converter
test = converter.Unicode()
import dataExtraction.fontconvert.bijoy_to_unicode as bijoy_to_unicode
import dataExtraction.fontconvert.stm as stm
import json
import dataExtraction.fontconvert.uniconverter as uniconverter
def pdf_to_text(path):
    fp = open(path, 'rb')
    text_dict={}
    '''manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)
        text_dict[0]=retstr.getvalue()
        retstr.flush()
        page_no+=1'''
    rsrcmgr = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    print(type(retstr))
    #laparams = LAParams()
    encoding = 'latin-1'
    device = TextConverter(rsrcmgr, retstr, codec='iso-8859-1', laparams=layout)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    page_no = 0
    for pageNumber, page in enumerate(PDFPage.get_pages(fp,check_extractable=False)):
        if pageNumber == page_no:
            interpreter.process_page(page)

            data = retstr.getvalue()
            u = json.dumps(data.decode('utf-8'), indent=4, ensure_ascii=True)
            text_dict[page_no]=u
            data = ''
            u=''
            retstr.truncate(0)
            retstr.seek(0)

        page_no += 1

    #text = retstr.getvalue()
    #pprint(text_dict)
    result_dict={}
    for key, value in sorted(text_dict.items()):
        splited_arr=value.split()
        arr=[]
        for val in splited_arr:
            #reslt=val.strip(' ')
            if(len(val)>2):
                arr.append(val)
        #pprint(arr)
        result_dict[key]=arr
    print('splited:')
    #pprint(result_dict)
    del text_dict
    for key,values in sorted(result_dict.items()):
        for value in values:
            print(value)
            con_v=stm.convert(value)
            print(con_v)




    #toUnicode = bijoy_to_unicode.convertBijoyToUnicode(text)
    #return bijoy_to_unicode.reArrangeUnicodeConvertedText(toUnicode)
    #st = json.dumps(text, ensure_ascii=True)
    #print(text)

    #txt='\xe0\xa6\xac\xe0\xa6\xab\xe0\xa6\xad\xe0\xa6\xbe\xe0\xa6\xa8'

    #u =json.dumps(text.decode("utf-8") ,indent=4,ensure_ascii=True)
    #print(u)
    toUnicode = bijoy_to_unicode.convertBijoyToUnicode(u)
    #print(toUnicode)
    uuu='\u00e0\u00a6\u00b8\u00e0\u00a7\u008d\u00e0\u00a6\u00a5\u00e0\u00a6\u00be\u00e0\u00a6\u00a9\u00e0\u00a6\u00a8\u00e0\u00a5\u00a4 '
    #t=stm.convert(u)
    #print(t)

    fp.close()
    device.close()
    retstr.close()
    return result_dict

def prefix_cutter(str,idx):
    return str[idx:]























