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

def date_digit_convert(txt):
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
    txt = txt.replace('.','-')
    txt = txt.replace('/','-')
    return txt

def month_convert(txt):
    if (not rules.jan_re.search(txt) == None or txt=='01'):
        return 'January'
    elif (not rules.feb_re.search(txt) == None or txt=='02'):
        return 'February'
    elif (not rules.mar_re.search(txt) == None or txt=='03'):
        return 'March'
    elif(not rules.apr_re.search(txt)==None or txt=='04'):
        return 'April'
    elif (not rules.may_re.search(txt) == None or txt=='05'):
        return 'May'
    elif (not rules.jun_re.search(txt) == None or txt=='06'):
        return 'June'
    elif (not rules.july_re.search(txt) == None or txt=='07'):
        return 'July'
    elif (not rules.agu_re.search(txt) == None or txt=='08'):
        return "August"
    elif (not rules.sep_re.search(txt) == None or txt=='09'):
        return 'September'
    elif (not rules.oct_re.search(txt) == None or txt=='10'):
        return 'October'
    elif (not rules.nov_re.search(txt) == None or txt=='11'):
        return 'November'
    elif(not rules.dec_re.search(txt)==None or txt=='12'):
        return 'December'

def division_convert(planning_division):
    if(not rules.agri_re.search(planning_division)==None):
        return 1
    if(not rules.energy_re.search(planning_division)==None):
        return 2
    if(not rules.structure_re.search(planning_division)==None):
        return 3
    if(not rules.social_re.search(planning_division)==None):
        return 4