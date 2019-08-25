import re
#project title rules
project_name_re=re.compile(r'প্রকল্পের\s*শিরোনাম|Project\s*(T|t)itle(s)?|প্রকল্পের\s*নাম|Name\s*of\s*the\s*Project' )
project_name_garbage_re=re.compile(r'সমজাতীয়|Same')
dpp_name_re=re.compile(r'উন্নয়ন\s*প্রকল্প\s*প্রস্তাব\s*\(ডিপিপি\)|উন্নয়ন\s*প্রকল্প\s*ছক,\s*প্রস্ত্মাব\s*\(ডিপিপি\)')
#Extimated cost rules
estimated_cost_re=re.compile(r'প্রকল্পের\s*প্রাক্কলিত\s*ব্যয়|প্রকল্পের\s*প্রক্কলিত\s*ব্যয়|প্রকল্প\s*ব্যয়|প্রকল্পের\s*ব্যয়|প্রকল্পের\s*প্রাক্কলিত\s*ব্যয়|প্রকল্পের\s*প্রাক্কলিত\s*ব্যয়|Estimated\s*(c|C)ost\s*of\s*the\s*((p|P)roject)?|মোট\s*প্রকল্প\s*ব্যয়')
investment_cost_re=re.compile(r'প্রকল্পের\s*প্রাক্কলিত\s*ব্যয়|মোট\s*প্রাক্কলিত\s*ব্যয়')
total_re=re.compile(r'মোট|Total|সবের্মাট')
gob_cost_re=re.compile(r'জিওবি|G(o|O)B|জওিবি|স্থানীয়\s*মুদ্রা|জওিব')
own_fund_re=re.compile(r'own\s*fund|সংস্থার\s*নিজস্ব\s*তহবিল|নজিস্ব\s*অর্থ|DNCC|নিজস্ব\s*অর্থ|Own\s*Fund|নিজস্ব\s*অর্থ|িজস্ব\s*অথর্|ঁuঁঁিনঁজঁস্ঁ্বঁ\s*ঁঅঁথঁর্ঁ|ঁuঁঁিনঁজঁস্ঁ্বঁ ঁঅঁথঁর্ঁ')
pa_cost_re=re.compile(r'PA|RPA|P.A|P.A.|প্রকল্প\s*সাহায্য')
other_cost_re=re.compile(r'অন্যান্য|(O|o)thers|অন্যান্য')
not_applicable_re=re.compile(r'প্রযোজ্য\s*নয়|নাই|-|00.00|০০.০০|প্রযোজ্য\s*নহে|মেয়াদ')
original_cost_re=re.compile(r'মূল\s*অনুমোদিত\s*ব্যয়|Original')
revised_cost_re=re.compile(r'সংশোধিত\s*প্রাক্কলিত\s*ব্যয়|1st\s*Revision')

amount_re=re.compile(r'(\d+|(০|১|২|৩|৪|৫|৬|৭|৮|৯)+).(\d+|(০|১|২|৩|৪|৫|৬|৭|৮|৯)+)')
clear_re=re.compile(r'\S+')
stop_cost_re=re.compile(r'বৈদেশিক|৫.২|5.2')
#project date rules
date_re=re.compile(r'প্রকল্পের\s*মেয়াদ|প্রকল্পের\s*বাস্তবায়নকালঃ|প্রকল্পের\s*বাস্ত্মবায়ন\s*কাল|প্রকল্পের\s*বাসত্মবায়নকাল|প্রকল্পের\s*বাস্ত্মবায়ন\s*কালঃ|প্রকল্পের\s*বাস্তবায়ন\s*কাল|প্রকল্প\s*বাস্ত্মবায়নকাল|প্রকল্পের\s*বাস্ত্মবায়নকাল|প্রকল্পের\s*মেয়াদ|Project\s*(i|I)mplementation\s*(p|P)eriod|প্রকল্পের\s*বাস্তবায়ণকাল')
start_date_re=re.compile(r'শুরম্নর\s*তারিখঃ|শুরুর\s*তারিখ| শুরম্নর\s*তারিখ|আরম্ভ|Date\s*of\s*(c|C)ommencement|Date\s*of\s*the\s*(c|C)ommencement|শুরম্নর\s*কাল|শুরুর\s*কাল')
end_date_re=re.compile(r'সমাপ্তির\s*তারিখ|সমাপ্তি|Date\s*of\s*(the)?\s*(c|C)ompletion|সমাপ্তির\s*কাল|সমাপ্তির\s*কাল')
mid_point_re=re.compile(r'থেকে|হতে|-')
year_re=re.compile(r'\d\d\d\d|(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)')
original_date_re=re.compile(r'মূল|Original')
revised_date_re=re.compile(r'সংশোধিত\s*\(১ম\)|Revised\s*\(1st\)')
date_format_re=re.compile(r'(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)|\d\d\d\d|(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)\s*(-|/)\s*(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)\s*(-|/|.)\s*(০|১|২|৩|৪|৫|৬|৭|৮|৯)(০|১|২|৩|৪|৫|৬|৭|৮|৯)|\d\d\s*(-|/|.)\s*\d\d\s*(-|/|.)\s*\d\d')

#responsible organization of project
point_re=re.compile(r'(\d|(০|১|২|৩|৪|৫|৬|৭|৮|৯)).(\d|(০|১|২|৩|৪|৫|৬|৭|৮|৯))')
ministy_re=re.compile(r'\tউদ্যোগী\s*মন্ত্রণালয়/বিভাগ\t|উদ্যোগী\s*মন্ত্রণালয়|উদ্যোগী\s*মন্ত্রণালয়\s*/\s*বিভাগ|উদ্যোগী\s*মন্ত্রণালয়/\s*বিভাগ|উদ্যোগী\s*মন্ত্রণালয়|Sponsoring\s*(M|m)inistry\s*/\s*Division|উদ্যোগী\s*মন্ত্রনালয়|Sponsoring/Ministry/Division|Sponsoring\s*Ministry|উদ্দ্যোগী\s*মন্ত্ম্রণালয়|Administrative\s*Ministry/Division')
partner_ministry_re=re.compile(r'Partner\s*Ministry')
agency_re=re.compile(r'\tবাস্তবায়নকারী\s*সংস্থা\s*(সংস্থাসমূহ)\t|বাস্ত্মবাযনকারী\s*সংস্থা|Executing\s*agency|বাসত্মবায়নকারী\s*সংস্থা|বাস্তবায়ণকারী\s*সংস্থা|বাস্তবায়নকারী\s*সংস্থা|বাস্ত্মবায়নকারী\s*সংস্থা|Executing\s*Agency|বাস্তাবায়নকারী\s*সংস্থা|Implementation\s*Agency|Implementing\s*Agency|Executing\s*Agency')
partner_agency_re=re.compile(r'Partner\s*Executing\s*Agency')
sector_re=re.compile(r'Concern\s*sector')
planning_re=re.compile(r'\tপরিকল্পনা\s*কমিশনের\s*সংশ্লিষ্ট\s*বিভাগ\t|(C|c)oncern(ed)?\s*(d|D)ivision\s*of\s*(p|P)lanning\s*(c|C)ommission|পরিকল্পনা কমিশনের সংশ্লিষ্ট বিভাগ|পরিকল্পনা\s*কমিশনের\s*(সংশ্লিষ্ট|সংশিস্নষ্ট)\s*বিভাগ|পরিকল্পনা\s*কমিশনের\s*সংশ্লিষ্ট\s*বিভাগ|Planning\s*Commission')
trackorg_re=re.compile(r'Objectives|Objectives\s*of\s*Project|প্রকল্পের\s*উদ্দেশ্য\s*ও\s*লক্ষ্যমাত্রা|cÖK‡íi\s*D‡Ïk¨|Objectives|প্রকল্পের\s*উদ্দেশ্য|মোট\s*প্রকল্প\s*ব্যয়|(O|o)bjective\s*of\s*the\s*(P|p)roject')
stop_org_re=re.compile(r'ব্যয়')
#objective of project
objective_re=re.compile(r'Objectives\s*of\s*the\s*project|প্রকল্পের\s*উদ্দেশ্য|Objectives\s*of\s*Project|প্রকল্পের\s*উদ্দেশ্য\s*ও\s*লক্ষ্যমাত্রা|cÖK‡íi\s*D‡Ïk¨|Objectives\s*and\s*Targets|প্রকল্পের\s*উদ্দেশ্য|(O|o)bjective\s*of\s*the\s*(P|p)roject')
stop_objective_re=re.compile(r'৪.০|4.0|প্রকল্পের\s*(প্রধান\s*প্রধান)?\s*কার্যক্রম|attach\s*map')
escape_objective_re=re.compile(r'বুলেট\s*আকারে|(W|w)rite\s*in\s*bullet\s*form')

#geo coverage

geo_re=re.compile(r'প্রকল্প\s*এলাকা|প্রকল্পভুক্ত\s*এলাকা|প্রকল্প\s*এলাকা|প্রকল্প\s*এলাকার\s*বিভাগ|(l|L)ocation\s*of\s*the\s*(p|P)roject(s)?|প্রকল্প\s*অবস্থান')
not_geo_re=re.compile(r'প্রকল্প\s*এলাকা\s*ভিত্তিতে|প্রকল্প\s*এলাকার\s*ব্যয়\s*বিভাজন|প্রকল্প\s*এলাকা\s*ভিত্তিক\s*ব্যয়\s*বিভাজন|প্রকল্প\s*এলাকার')
stop_geo_re=re.compile(r'প্রাক্কলিত\s*ব্যয়ের|(L|l)ocation-wise\s*(C|c)ost\s*(B|b)reakdown|Cost\s*Breakdown|cost|ব্যয়\s*বিভাজন ')
#project activity
activity_re=re.compile(r'প্রকল্প\s*(প্রধান\s*প্রধান)?\s*কার্যক্রম|\d\d.\d\s*Activities')
stop_activity_re=re.compile(r'(সপ্তম|৭ম)\s*পঞ্চবার্ষিক|প্রকল্প\s*সংগতিপূর্ণতা|প্রকল্প\s*এলাকা')
stop_activity_re_1=re.compile(r'(\d)?\d.\d|(০|১|২|৩|৪|৫|৬|৭|৮|৯)?(০|১|২|৩|৪|৫|৬|৭|৮|৯).(০|১|২|৩|৪|৫|৬|৭|৮|৯)')