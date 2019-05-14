#!/usr/bin/env python
# -*- coding: utf-8 -*-

def convert(txt):
    import re

    ## Ensre unicode input text
    # txt = txt.decode('utf-8')

    ## Block 0 : The Deletables!
    txt = txt.replace('\u0020', ' ')  # space

    txt = txt.replace('\u00e9', '')
    txt = txt.replace('\u00f9', '')
    txt = txt.replace('\u00fe', '')

    txt = txt.replace('\u00ec', '')

    ## Block 1 : Single character of OP formed using two partial INPUT characters
    # ~ txt = txt.replace('\u00ee\u00fb\u002a','রূ') ## added on 15/01/2015
    txt = txt.replace('\u00dd\u00c6', 'ট্র')  ## added on 15/01/2015
    txt = txt.replace('\u00c1\u00b1', 'ম্প্র')  ## added on 15/01/2015
    # ~ txt = txt.replace('\u00c1\u00b1','X') ## added on 15/01/2015

    txt = txt.replace('\u00ee\u00fb', 'র')
    txt = txt.replace('\u00eb\u00fb', 'য়')
    txt = txt.replace('\u0078\u0079', 'আ')
    txt = txt.replace('\u0076\u007a', 'উ')
    txt = txt.replace('\u00a3\u007a', 'ই')
    txt = txt.replace('\u007e\u0152', 'ঞ')
    txt = txt.replace('\u0065\u00ab', 'ক্র')
    txt = txt.replace('\u005f\u00ab', 'ক্ত')
    txt = txt.replace('\u00a3\u00ab', 'হ্ন')

    ## SPECIALS (HACKS)!!!
    # ~ txt = txt.replace('\u0073\u0069','ন্থ')
    txt = txt.replace('\u0073 \u0069', 'ন্থ')
    txt = txt.replace('\u00c1\u00ac', 'ম্ন')
    txt = txt.replace('\u00a7\u00ac', 'ন্ন')  # added on 15/01/2015
    txt = txt.replace('\u0046\u0160', 'চ্ছ')  # added on 15/01/2015
    txt = txt.replace('\u00b2\u00cc\u0026', 'প্রু')

    ## Added 15/01/2015
    txt = txt.replace('\u0021\u00df\u0066', 'স্ত্রি')
    txt = txt.replace('\u00df\u0066', 'স্ত্র')

    txt = txt.replace('\u0021\u00df\u00ac', 'স্নি')
    txt = txt.replace('\u00df\u00ac', 'স্ন')
    # ~ txt = txt.replace('\u00df\u00f1','স্ক')
    txt = txt.replace('\u00df\u0025\u00f1', 'স্কু')
    txt = txt.replace('\u00df\u00f1\u0025', 'স্কু')
    txt = txt.replace('\u0073\u0066', 'ন্ত্র')

    txt = txt.replace('\u201e\u00cf', 'ক্ল')  # added on 15/01/2015
    txt = txt.replace('\u0161\u00cf', 'ফ্ল')
    # ~ txt = txt.replace('\u00de\u0069','স্থ')
    # ~ txt = txt.replace('\u00df\u0069','স্থ')

    txt = txt.replace('\u0021\u00df\u0054\u00c9', 'স্ট্রি')
    txt = txt.replace('\u0021\u00df\u0054\u00c9', 'স্ট্রে')
    txt = txt.replace('\u0021\u00df\u0054\u00c9', 'স্ট্রৈ')

    txt = re.compile(r'(.)\u0069').sub(r'\1থ', txt)

    txt = txt.replace('\u2039\u00b5', 'জ্ব')  # added on 15/01/2015
    txt = re.compile(r'\u0067(.)').sub(r'\1ত্ব', txt)
    txt = re.compile(r'\u0068(.)').sub(r'\1ত', txt)
    # ~ ‌‌added on 15/01/2015
    txt = re.compile(r'\u006c(.)').sub(r'\1তু', txt)

    ## Block 2A : OP formed from single INPUT character : SWARABARNAS
    txt = txt.replace('\u0078', 'অ')
    txt = txt.replace('\u007B', 'ঈ')
    txt = txt.replace('\u007C', 'ঊ')
    txt = txt.replace('\u007D', 'ঋ')
    txt = txt.replace('\u007E', 'এ')
    txt = txt.replace('\u00fa', 'ঐ')
    txt = txt.replace('\u00E7', 'ও')
    txt = txt.replace('\u00E8', 'ঔ')
    txt = txt.replace('\u007F', '৺')

    ## Block 2B : OP formed from single INPUT character : BYANJANS with MATRA/KAAR
    txt = txt.replace('\u00fd', 'হু')
    txt = txt.replace('\u003d', 'গু')

    ## Block 2C : OP formed from single INPUT character : BYANJANBARNAS
    txt = txt.replace('\u2018\u00fc', 'ঢ়')  ## added on 16/01/2015
    txt = txt.replace('\u0076\u00fc', 'ড়')
    txt = txt.replace('\u0047', 'ঝ')
    txt = txt.replace('\u0048', 'ছ')  ##???
    txt = txt.replace('\u0057', 'ঢ')  ## ???
    txt = txt.replace('\u0076', 'ড')
    txt = txt.replace('\u00a1', 'ষ')
    txt = txt.replace('\u00a2', 'স')
    txt = txt.replace('\u00a3', 'হ')
    txt = txt.replace('\u00a6', 'ভ')
    txt = txt.replace('\u00dd', 'ট')
    txt = txt.replace('\u00e0', 'ঠ')
    txt = txt.replace('\u00ea', 'ৎ')
    txt = txt.replace('\u00eb', 'য')
    txt = txt.replace('\u00ed', 'থ')
    txt = txt.replace('\u00ee', 'ব')
    txt = txt.replace('\u00b9', 'ব')
    txt = txt.replace('\u0153', 'ল')
    txt = txt.replace('\u0160', 'ছ')
    txt = txt.replace('\u0161', 'ফ')
    txt = txt.replace('\u0178', 'শ')
    txt = txt.replace('\u0192', 'ঃ')
    txt = txt.replace('\u02c6', 'ঙ')
    txt = txt.replace('\u02dc', 'ন')
    txt = txt.replace('\u2018', 'ঢ')
    txt = txt.replace('\u2019', 'ণ')
    txt = txt.replace('\u201a', 'ং')
    txt = txt.replace('\u201c', 'ত')
    txt = txt.replace('\u201d', 'দ')
    txt = txt.replace('\u201e', 'ক')
    txt = txt.replace('\u2020', 'গ')
    txt = txt.replace('\u2021', 'ঘ')
    txt = txt.replace('\u2022', 'ধ')
    txt = txt.replace('\u2026', 'খ')
    txt = txt.replace('\u2030', 'চ')
    txt = txt.replace('\u2039', 'জ')
    txt = txt.replace('\u203a', 'ম')
    txt = txt.replace('\u2122', 'প')

    ## Block 2D : OP formed from single INPUT character : JUKTAKHYORS
    txt = txt.replace('\u0022', 'ক্ষ্ম')
    txt = txt.replace('\u002d', 'ঙ্ম')
    txt = txt.replace('\u003a', 'ক্স')
    txt = txt.replace('\u00c7', 'ক্ষ')
    txt = txt.replace('\u003e', 'গ্গ')
    txt = txt.replace('\u003f', 'গ্ধ')
    txt = txt.replace('\u0042', 'ঙ্ক')
    txt = txt.replace('\u0043', 'ঙ্খ')
    txt = txt.replace('\u0044', 'ঙ্গ')
    txt = txt.replace('\u0045', 'ক্ক')
    txt = txt.replace('\u0049', 'জ্জ')
    txt = txt.replace('\u004a', 'জ্ঝ')
    txt = txt.replace('\u004b', 'জ্ঞ')
    txt = txt.replace('\u004c', 'জ্র')
    txt = txt.replace('\u004d', 'ঞ্চ')
    txt = txt.replace('\u004e', 'ঞ্ছ')
    txt = txt.replace('\u004f', 'ঞ্জ')
    txt = txt.replace('\u0050', 'ঞ্ঝ')
    txt = txt.replace('\u0051', 'ক্ট')
    txt = txt.replace('\u0052', 'ট্ট')
    txt = txt.replace('\u0055', 'ড্ড')
    txt = txt.replace('\u005a', 'ণ্ঠ')
    txt = txt.replace('\u005b', 'ণ্ড')
    txt = txt.replace('\u005c', 'ণ্ড্র')
    txt = txt.replace('\u005d', 'ণ্ন')
    txt = txt.replace('\u005f', 'ত্ত')
    txt = txt.replace('\u0060', 'ক্ত্র')  ## ????
    txt = txt.replace('\u0061', 'ত্থ')
    txt = txt.replace('\u0062', 'ত্ন')
    txt = txt.replace('\u0063', 'ত্ব')
    txt = txt.replace('\u0064', 'ত্ম')
    txt = txt.replace('\u0065', 'ত্র')
    txt = txt.replace('\u006a', 'দ্দ')
    txt = txt.replace('\u006b', 'দ্ধ')
    txt = txt.replace('\u006d', 'দ্ব')
    txt = txt.replace('\u006f', 'দ্র')
    txt = txt.replace('\u0070', 'দ্ম')
    txt = txt.replace('\u0071', 'দ্ভ')
    txt = txt.replace('\u0074', 'ন্ঠ')
    txt = txt.replace('\u0075', 'ন্ড')
    txt = txt.replace('\u0077', 'ন্দ্র')
    txt = txt.replace('\u00a8', 'ন্দ')
    txt = txt.replace('\u00a9', 'ক্ম')
    txt = txt.replace('\u00aa', 'ন্স')
    txt = txt.replace('\u00ae', 'প্ত')
    txt = txt.replace('\u00af', 'প্প')
    txt = txt.replace('\u00b0', 'প্স')
    txt = txt.replace('\u00b1', 'প্র')
    txt = txt.replace('\u00b6', 'ব্জ')
    txt = txt.replace('\u00b7', 'ব্দ')
    txt = txt.replace('\u00b8', 'ব্ধ')
    txt = txt.replace('\u00bc', 'ভ্র')
    txt = txt.replace('\u00bd', 'ম্ভ')
    txt = txt.replace('\u00be', 'ম্ভ্র')
    txt = txt.replace('\u00d1', 'ল্গ')
    txt = txt.replace('\u00d2', 'ল্প')
    txt = txt.replace('\u00d3', 'ল্ড')
    txt = txt.replace('\u00d6', 'শু')
    txt = txt.replace('\u00d7', 'শ্র')
    txt = txt.replace('\u00d8', 'শ্চ')
    txt = txt.replace('\u00db', 'ষ্ঠ')
    txt = txt.replace('\u00e1', 'হ্ম')
    txt = txt.replace('\u00e2', 'হ্ল')
    txt = txt.replace('\u00e3', 'হ্ণ')
    txt = txt.replace('\u00f5', 'ন্ধ')
    txt = txt.replace('\u20ac', 'ল্গু')

    ## Block 3A : Partial OP character from single partial INPUT character : LEFT appear (to be ligatre-d on OP)
    txt = txt.replace('\u0040', 'গ্')
    txt = txt.replace('\u0041', 'ঙ্')
    txt = txt.replace('\u0046', 'চ্')
    txt = txt.replace('\u0058', 'ড়্‌')
    txt = txt.replace('\u005e', 'ণ্‌')
    txt = txt.replace('\u0072', 'ন্')
    txt = txt.replace('\u00a7', 'ন্')
    txt = txt.replace('\u0073 ', 'ন্')  #####
    txt = txt.replace('\u0073', 'ন্')
    txt = txt.replace('\u00b2', 'প্')
    txt = txt.replace('\u00c1', 'ম্')
    txt = txt.replace('\u00cd', 'ল্')
    txt = txt.replace('\u00ce', 'ল্')
    txt = txt.replace('\u00d9', 'শ্')
    txt = txt.replace('\u00dc', 'ষ্')
    txt = txt.replace('\u00de', 'স্')
    txt = txt.replace('\u00df', 'স্')
    txt = txt.replace('\u00e5', 'দ্')

    ## Block 3A : Partial OP character from single partial INPUT character : RIGHT appear (to be ligatre-d on OP)
    # txt = txt = re.compile(r'(.)\u00').sub(r'\1',txt)
    txt = re.compile(r'(.)\u003b').sub(r'\1ক্র', txt)
    txt = re.compile(r'(.)\u003c').sub(r'\1‌খ', txt)
    txt = re.compile(r'(.)\u0054').sub(r'\1ট', txt)
    txt = re.compile(r'(.)\u0066').sub(r'‌\1ত্র', txt)
    txt = re.compile(r'(.)\u006c').sub(r'\1‌ত্ত', txt)
    txt = re.compile(r'(.)\u00ac').sub(r'\1‌ন', txt)
    txt = re.compile(r'(.)\u00b3').sub(r'\1ফ', txt)
    txt = re.compile(r'(.)\u00b4').sub(r'\1ব', txt)
    txt = re.compile(r'(.)\u00b5').sub(r'\1ব', txt)
    txt = re.compile(r'(.)\u00ba').sub(r'\1ব', txt)
    txt = re.compile(r'(.)\u00bb').sub(r'\1ব', txt)
    txt = re.compile(r'(.)\u00bf').sub(r'\1ম', txt)
    txt = re.compile(r'(.)\u00c0').sub(r'\1ণ', txt)
    txt = re.compile(r'(.)\u00c2').sub(r'ম', txt)
    txt = re.compile(r'(.)\u00c3').sub(r'\1ম', txt)
    txt = re.compile(r'(.)\u00cf').sub(r'\1ল', txt)
    txt = re.compile(r'(.)\u00d4').sub(r'\1ল', txt)
    txt = re.compile(r'(.)\u00d5').sub(r'\1ল', txt)
    txt = re.compile(r'(.)\u00f1').sub(r'\1ক', txt)
    txt = re.compile(r'(.)\u00f8').sub(r'\1ন', txt)

    ## Block 4 : Ref, fola-s, matra-s
    # ~ txt =  txt.replace('\u00a4','ঁ')
    # ~ txt =  txt.replace('\u00a5','ঁ')

    ## Chandrabindu (added here on 15/01/2015)
    txt = re.compile(r'(.)\u00a4\u00c4\u0079').sub(r'\1্যাঁ', txt)
    txt = re.compile(r'(.)\u00a5\u00c4\u0079').sub(r'\1্যাঁ', txt)
    # ঁ  া  ্য ্ঁ
    txt = re.compile(r'(.)\u00a4\u0079').sub(r'\1াঁ', txt)
    txt = re.compile(r'(.)\u00a5\u0079').sub(r'\1াঁ', txt)
    txt = re.compile(r'\u00f6(.)\u00a4\u00ef').sub(r'\1ৌঁ', txt)
    txt = re.compile(r'\u00f6(.)\u00a5\u00ef').sub(r'\1ৌঁ', txt)

    txt = re.compile(r'(.)\u00c5').sub(r'র্\1', txt)  ## Ref

    txt = re.compile(r'(.)\u00cc').sub(r'\1র‌', txt)  ## ro-fola-s
    txt = re.compile(r'(.)\u00cb').sub(r'\1র‌', txt)
    txt = re.compile(r'(.)\u00ca').sub(r'\1র‌', txt)
    txt = re.compile(r'(.)\u00c9').sub(r'\1র‌', txt)
    txt = re.compile(r'(.)\u00c8').sub(r'\1র‌', txt)
    txt = re.compile(r'(.)\u00c6').sub(r'\1র‌', txt)

    ## jaw-fola (addded on 15/01/2015)
    txt = re.compile(r'(.)\u0025\u00c4').sub(r'\1্যু', txt)
    txt = re.compile(r'(.)\u00c4').sub(r'\1্য', txt)
    # ~ txt = txt.replace('\u00c4','্য') ## jaw-fola

    ## Block 5A : kaar-s (left appears)
    txt = re.compile(r'\u00f6(.)\u0079').sub(r'\1ো', txt)
    txt = re.compile(r'\u00f6(.)\u00ef').sub(r'\1ৌ', txt)
    # ~ txt = re.compile(r'\u00f6(.*)\u0079\u007a').sub(r'\1ৌ',txt)

    txt = re.compile(r'\u0021(.্‌?.?)').sub(r'\1ি', txt)  ## For juktakhyors
    txt = re.compile(r'\u0021(.)').sub(r'\1ি', txt)

    txt = re.compile(r'\u00f6(.্‌?.?)').sub(r'\1ে', txt)  ## For juktakhyors
    txt = re.compile(r'\u00f6(.)').sub(r'\1ে', txt)

    txt = re.compile(r'\u00f7(.্‌?.?)').sub(r'\1ৈ', txt)  ## For juktakhyors
    txt = re.compile(r'\u00f7(.)').sub(r'\1ৈ', txt)

    ## Block 5B : Kaar-s (Right Appears)
    txt = txt.replace('\u0079', 'া')
    txt = txt.replace('\u0023', 'ী')
    txt = txt.replace('\u0024', 'ু')
    txt = txt.replace('\u0025', 'ু')
    txt = txt.replace('\u0026', 'ু')
    txt = txt.replace('\u0028', 'ূ')
    txt = txt.replace('\u0029', 'ূ')
    txt = txt.replace('\u002a', 'ূ')  # added on 15/01/2015
    txt = txt.replace('\u002b', 'ৃ')
    txt = txt.replace('\u002c', 'ৃ')

    ## Block 6 : OP formed from single INPUT character : NUMERALS & PUNCTUATIONS
    txt = txt.replace('\u0030', '০')
    txt = txt.replace('\u0031', '১')
    txt = txt.replace('\u0032', '২')
    txt = txt.replace('\u0033', '৩')
    txt = txt.replace('\u0034', '৪')
    txt = txt.replace('\u0035', '৫')
    txt = txt.replace('\u0036', '৬')
    txt = txt.replace('\u0037', '৭')
    txt = txt.replace('\u0038', '৮')
    txt = txt.replace('\u0039', '৯')

    txt = txt.replace('\u002f', '/')
    txt = txt.replace('\u0053', '(')
    txt = txt.replace('\u0056', ')')
    txt = txt.replace('\u00a0', '*')
    txt = txt.replace('\u00ad', ':')
    txt = txt.replace('\u00d0', '।')
    txt = txt.replace('\u00da', '?')
    txt = txt.replace('\u00e6', '!')
    txt = txt.replace('\u00f2', '‘')
    txt = txt.replace('\u00f3', '’')
    txt = txt.replace('\u00f4', '-')
    txt = txt.replace('\u2013', ',')
    txt = txt.replace('\u2014', ';')

    txt = txt.replace('\u00e4', '্‌')  ## added on 16/01/2015

    ## Chandrabindu
    txt = txt.replace('\u00a4', 'ঁ')
    txt = txt.replace('\u00a5', 'ঁ')

    return txt
