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
    txt = txt.replace(',', '')
    txt = txt.replace(' ', '')
    return txt

def month_convert(txt):
    if (not rules.jan_re.search(txt) == None or txt=='01'):
        return 'Jan'
    elif (not rules.feb_re.search(txt) == None or txt=='02'):
        return 'Feb'
    elif (not rules.mar_re.search(txt) == None or txt=='03'):
        return 'Mar'
    elif(not rules.apr_re.search(txt)==None or txt=='04'):
        return 'Apr'
    elif (not rules.may_re.search(txt) == None or txt=='05'):
        return 'May'
    elif (not rules.jun_re.search(txt) == None or txt=='06'):
        return 'Jun'
    elif (not rules.july_re.search(txt) == None or txt=='07'):
        return 'July'
    elif (not rules.agu_re.search(txt) == None or txt=='08'):
        return "Aug"
    elif (not rules.sep_re.search(txt) == None or txt=='09'):
        return 'Sep'
    elif (not rules.oct_re.search(txt) == None or txt=='10'):
        return 'Oct'
    elif (not rules.nov_re.search(txt) == None or txt=='11'):
        return 'Nov'
    elif(not rules.dec_re.search(txt)==None or txt=='12'):
        return 'Dec'
