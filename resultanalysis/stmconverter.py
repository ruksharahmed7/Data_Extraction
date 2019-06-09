import dataExtraction.rulesfile.convertingrules as rules

def digit_convert(txt):
    txt = txt.replace('০', '0')
    txt = txt.replace('১', '1')
    txt = txt.replace('২','2')
    txt = txt.replace('৩','3')
    txt = txt.replace('৪', '4')
    txt = txt.replace('৫','5')
    txt = txt.replace('৬','6')
    txt = txt.replace('৭', '7')
    txt = txt.replace('৮', '8')
    txt = txt.replace('৯', '9')
    txt = txt.replace('.','.')
    txt = txt.replace(',', '.')
    txt = txt.replace(' ', '')
    return txt

def month_convert(txt):
    if(not rules.july_re.search(txt)==None):
        return 6
    elif(not rules.dec_re.search(txt)==None):
        return 12
