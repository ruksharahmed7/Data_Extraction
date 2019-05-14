"""import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=False):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text"""

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import pdftotext

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams(),codec='ascii')
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


from PyPDF2 import PdfFileReader


def extract_pdf(filename):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)


    print(pdfReader.numPages)

    pageObj = pdfReader.getPage(0)
    pagecontent = pageObj.extractText()

    pdfContent = StringIO(getPDFContent(filename).copy())
    for line in pdfContent:
        print(line.strip())

    return pagecontent

def getPDFContent(path):
    with open(path, "rb") as f:
        pdf = pdftotext.PDF(f)
    content=[]
    for page in pdf:
        content.append(page)
    return content