import re

date_formate_re=re.compile(r'(\d\d).(\d\d).(\d\d\d\d)|((০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)).((০|১)(০|১|২|৩|৪|৫|৬|৭|৮|৯)).((০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯))')
division_re=re.compile(r'বিভাগ\s*:|বিভাগ:')
point_re=re.compile(r'(\d\d).\s|((০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)).\s')
cost_value_re=re.compile(r'\d+.\d+|(০|১|২|৩|৪|৫|৬|৭|৮|৯)+.(০|১|২|৩|৪|৫|৬|৭|৮|৯)+')
estimated_cost_re=re.compile(r'প্রকল্পটির\s*প্রাক্কলিত\s*ব্যয়|প্রাক্কলিত\s*ব্যয়|প্রকল্পটির প্রাক্কলিত ব্যয়|প্রাক্কলিত\s*ব্যয়')
total_re=re.compile(r'মোট')
total_suplimentary_re=re.compile(r'হয়েছে|ব্যয়')
and_re=re.compile(r'এবং|\(|তন্মধ্যে')
project_date_re=re.compile(r'বাস্তবায়নকাল|বাস্তবায়নকাল')
from_re=re.compile(r'হতে|থেকে')
year_re=re.compile(r'\d\d\d\d|(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)')

activity_re=re.compile(r'প্রকল্পটির\s*প্রধান\s*কার্যক্রমসমূহ|কার্যক্রমসমূহ')


#clustering rules
starting_re=re.compile(r'আলোচ্য\s*বিষয়')
stopping_re=re.compile(r'পরিকল্পনার\s*সাথে\s*সংগতিপূর্ণতা|পিইসি\s*সভা|প্রকল্প\s*সংশোধনের\s*কারণ')

#brief summary rules
stop_point_re=re.compile(r'\d(\d).|(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)?.')

project_name_re=re.compile(r'প্রকল্পের\s*নাম')
ministy_re=re.compile(r'উদ্যোগী\s*মন্ত্রণালয়|উদ্যোগী\s*মন্ত্রণালয়\s*/\s*বিভাগ|উদ্যোগী\s*মন্ত্রণালয়/\s*বিভাগ|উদ্যোগী\s*মন্ত্রণালয়|Sponsoring\s*Ministry\s*/\s*Division|উদ্যোগী\s*মন্ত্রনালয়|Sponsoring/Ministry/Division|Sponsoring\s*Ministry|উদ্দ্যোগী\s*মন্ত্ম্রণালয়|Administrative\s*Ministry/Division')
agency_re=re.compile(r'বাসত্মবায়নকারী\s*সংস্থা|বাস্তবায়ণকারী\s*সংস্থা|বাস্তবায়নকারী\s*সংস্থা|বাস্ত্মবায়নকারী\s*সংস্থা|Executing\s*Agency|বাস্তাবায়নকারী\s*সংস্থা|Implementation\s*Agency|Implementing\s*Agency|Executing\s*Agency')
objective_re=re.compile(r'প্রকল্পের\s*উদ্দেশ্য|Objectives\s*of\s*Project|প্রকল্পের\s*উদ্দেশ্য\s*ও\s*লক্ষ্যমাত্রা|cÖK‡íi\s*D‡Ïk¨|Objectives\s*and\s*Targets|প্রকল্পের\s*উদ্দেশ্য|(O|o)bjective\s*of\s*the\s*(P|p)roject')
location_re=re.compile(r'প্রকল্প\s*এলাকা|প্রকল্প\s*এলাকার\s*বিভাগ|(l|)Location\s*of\s*the\s*(p|P)roject(s)?|প্রকল্প\s*অবস্থান')
date_re=re.compile(r'বাস্তবায়নকাল|প্রকল্পের\s*বাস্তবায়নকালঃ|প্রকল্পের\s*বাস্ত্মবায়ন\s*কাল|প্রকল্পের\s*বাসত্মবায়নকাল|প্রকল্পের\s*বাস্ত্মবায়ন\s*কালঃ|প্রকল্পের\s*বাস্তবায়ন\s*কাল|প্রকল্প\s*বাস্ত্মবায়নকাল|প্রকল্পের\s*বাস্ত্মবায়নকাল|প্রকল্পের\s*মেয়াদ|Project\s*(i|I)mplementation\s*(p|P)eriod|প্রকল্পের\s*বাস্তবায়ণকাল')
activity_re=re.compile(r'প্রকল্প\s*(প্রধান\s*প্রধান)?\s*কার্যক্রম|প্রধান\s*কার্যক্রমসমূহ')
total_re=re.compile(r'মোট|Total|সবের্মাট|মোট\s*প্রকল্প\s*ব্যয়')
gob_cost_re=re.compile(r'জিওবি|G(o|O)B|জওিবি|স্থানীয়\s*মুদ্রা|জওিব')
pa_cost_re=re.compile(r'PA|RPA|P.A|P.A.|প্রকল্প\s*সাহায্য')
own_fund_re=re.compile(r'সংস্থার\s*নিজস্ব\s*তহবিল|নজিস্ব\s*অর্থ|DNCC|নিজস্ব\s*অর্থ|Own\s*Fund|নিজস্ব\s*অর্থ|িজস্ব\s*অথর্|ঁuঁঁিনঁজঁস্ঁ্বঁ\s*ঁঅঁথঁর্ঁ|ঁuঁঁিনঁজঁস্ঁ্বঁ ঁঅঁথঁর্ঁ')

