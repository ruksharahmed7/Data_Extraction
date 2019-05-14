from pdfminer.converter import TextConverter
from io import StringIO
from io import open
from urllib.request import urlopen

from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from io import BytesIO

def readPDF(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    device.close()
    retstr.close()
    return text
def extract(pdfpath):
    outputString=readPDF(pdfpath)
    proceedings=str(outputString)
    with open('output.txt', 'w', encoding="utf-8") as proceedings_file:
        proceedings_file.write(proceedings)