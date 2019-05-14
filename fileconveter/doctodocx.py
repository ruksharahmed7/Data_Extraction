import subprocess
import os

def doc_to_docx_converting(file):
    subprocess.call(['soffice', '--headless', '--convert-to', 'docx', file], shell = True)
    print('converted')