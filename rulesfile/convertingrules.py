import re

#cost converting
number_re=re.compile(r'(\d+|(০|১|২|৩|৪|৫|৬|৭|৮|৯)+).(\d+|(০|১|২|৩|৪|৫|৬|৭|৮|৯)+)')
lakh_re=re.compile(r'লক্ষ|Lac|Lakh|লÿ')
core_re=re.compile(r'কোটি')


#date converting
date_formate_1_re=re.compile(r'(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)\s*(-|/|\|.)\s*(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)\s*(-|/|.)\s*((০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯))?(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)|\d\d\s*(-|/|.)\s*\d\d\s*(-|/|.)\s*(\d\d)?\d\d')
year_formate_re=re.compile(r'(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)|\d\d\d\d')
jan_re=re.compile(r'জানুয়ারী|জানুয়ারি|January|জানুয়ারি')
feb_re=re.compile(r'ফেব্রুয়ারী|February')
mar_re=re.compile(r'মার্চ|March')
apr_re=re.compile(r'এপ্রিল|April')
may_re=re.compile(r'মে|May')
jun_re=re.compile(r'জুন|জুন|June')
july_re=re.compile(r'জুলাই|July')
agu_re=re.compile(r'আগষ্ট|August|আগস্ট')
sep_re=re.compile(r'সেপ্টেম্বর|September')
oct_re=re.compile(r'অক্টোবর|October')
nov_re=re.compile(r'নভেম্বর|November')
dec_re=re.compile(r'ডিসেম্বর|December')
#approval date converting rules
date_formate_goal=re.compile(r'\d\d(-)\d\d(-)\d\d\d\d')
day_re=re.compile(r'(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)|(০|১|২|৩|৪|৫|৬|৭|৮|৯)|\d\d|\d')

#planning division convertion
agri_re=re.compile(r'কৃষি|পানি|পলস্নী|পল্লী|ফসল')
energy_re=re.compile(r'শিল্প|শক্তি|Industries|Energy')
structure_re=re.compile(r'ভৌত|আবকাঠামো|Physical|Infrastructure')
social_re=re.compile(r'আর্থ|সামাজিক')

