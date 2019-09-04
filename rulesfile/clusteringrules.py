import re
start_re=re.compile(r'উন্নয়ন\s*প্রকল্প\s*প্রস্তাব')

project_name_re=re.compile(r'প্রকল্প\s*শিরোনাম|প্রকল্প\s*নাম|(P|p)roject\s*(T|t)itle')
project_cost_re=re.compile(r'মোট\s*প্রকল্প\s*ব্যয়|প্রকল্প\s*প্রাক্কলিত\s*ব্য|প্রকল্প\s*প্রাক্কলিত\s*ব্য|Estimated\s*(C|c)ost\s*of\s*the\s*(p|P)roject')
ministry_re=re.compile(r'উদ্যোগী\s*মন্ত্রণাল\s*/\s*বিভাগ|উদ্যোগী\s*মন্ত্রণাল\s*/\s*বিভাগ|Sponsoring\s*Ministry\s*/\s*Division')
agency_re=re.compile(r'বাস্তবায়নকারী\s*সংস্থা|Implementing\s*Agency')
planning_division_re=re.compile(r'পরিকল্পনা\s*কমিশন\s*সংশ্লিষ্ট\s*বিভাগ|Concerned\s*Division\s*of\s*Planning\s*commission')
date_re=re.compile(r'প্রকল্প\s*মেয়াদ|প্রকল্পের\s*মেয়াদ|প্রকল্প\s*বাস্ত্মবায়নকাল|প্রকল্প\s*বাস্তবায়ন\s*কাল|Project\s*Implementation\s*Period')
point_re=re.compile(r'((০|১|২|৩|৪|৫|৬|৭|৮|৯)\s*.\s*(০|১|২|৩|৪|৫|৬|৭|৮|৯))')
objective_re=re.compile(r'প্রকল্প\s*উদ্দেশ্য|প্রকল্প\s*উদ্দেশ্য\s*লক্ষমাত্|প্রকল্পের\s*উদ্দেশ্য\s*ও\s*লÿ্যমাত্রা|প্রকল্প\s*উদ্দেশ্য\s*লক্ষ্যমাত্|Objectives\s*and\s*Targets|cÖK‡íi D‡Ïk')
stop_objective_re=re.compile(r'সংক্ষিপ্ত\s*পটভূমি')
type_re=re.compile(r'বৈদেশিক\s*মূদ্র\s*বিনিম|বৈদেশিক\s*মূদ্রার\s*বিনিয়োগ\s*হার|অর্থায়ন\s*ধরন\s*উৎস|বৈদেশিক\s*(মূদ্র|মুদ্র)\s*(বিনিয়োগ|বিনিম)\s*হ|Mode\s*of\s*Financing\s*with\s*source|Mode\s*of\s*Financing')
geo_re=re.compile(r'প্রকল্প\s*এলাকা|প্রকল্প\s*এলাকার\s*বিভাগ|Location\s*of\s*the\s*Projects|প্রকল্প\s*অবস্থান')
geo_stop_re=re.compile(r'প্রকল্প\s*এলাকার\s*মানচিত্র|প্রকল্প\s*সম্ভাব্যতা\s*যাচা|প্রকল্প\s*এলাকাভিত্তিক|মানচিত্র\s*প্রকল্প\s*অবস্থান\s*চিহ্নিত|Attach\s*map|প্রকল্প \s*এলাকার\s*মানচিত্র|মানচিত্র\s*সংযুক্ত|প্রযোজ্য\s*মানচিত্র\s*সংযুক্ত|প্রকল্প\s*এলাকাভিত্তিক\s*ব্য\s*বিভাজন\s*(সংযোজনী)?|প্রকল্প\s*উদ্দেশ্য')
not_geo_re=re.compile(r'নির্বাচন\s*যৌক্তিকতা')
activity_re=re.compile(r'প্রকল্প\s*(প্রধান\s*প্রধান)?\s*কার্যক্রম')

final_clustering_re=re.compile(r'প্রকল্পের\s*অবস্থান|প্রকল্প\s*এলাকা|প্রকল্প\s*এলাকার\s*বিভাগ|Location\s*of\s*(T|t)he\s*(P|p)rojects')