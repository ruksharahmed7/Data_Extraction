import re
#clustering rules
start_re=re.compile(r'(\d|(০|১|২|৩|৪|৫|৬|৭|৮|৯))\s*.\s*(আলোচ্য\s*বিষয়|আলোচ্য)')
catch_re=re.compile(r'উপস্থাপনা\s*ও\s*আলোচনা')
decision_re=re.compile(r'সিদ্বান্ত|সিদ্ধান্তঃ|সিদ্ধান্ত:|সিদ্ধান্ত')
ministry_start_re=re.compile(r'মাননীয়\s*মন্ত্রী(,)?\s*পরিকল্পনা\s*মন্ত্রণালয়\s*কর্তৃক\s*অনুমোদিত')


#extraction rules
approved_re=re.compile(r'অনুমোদন\s*করা\s*হল')
unapproved_re=re.compile(r'অনুমোদন\s*করা\s*হল\s*না')
total_gob_re=re.compile(r'সম্পূর্ণ\s*জিওবি\s*অর্থায়নে')
total_re=re.compile(r'মোট')
gob_re=re.compile(r'জিওবি')
own_fund_re=re.compile(r'সংস্থার\s*নিজস্ব\s*তহবিল|সংস্থার\s*নিজেস্ব\s*তহবিল|নিজস্ব\s*অথার্য়ন|নিজস্ব\s*তহবিল')
pa_re=re.compile(r'প্রকল্প\s*সাহায্য|প্রকল্প\s*সাহায্য|প্রকল্প\s*ঋণ')
and_re=re.compile(r'এবং')
amount_re=re.compile(r'(\d+|(০|১|২|৩|৪|৫|৬|৭|৮|৯)+).(\d+|(০|১|২|৩|৪|৫|৬|৭|৮|৯)+)')
track1_re=re.compile(r'প্রাক্কলিত\s*ব্যয়ে|প্রক্কলিত\s*ব্যয়ে| প্রাক্কলিত\s*ব্যয়|প্রাক্কলিত\s*ব্যয়ে')
track2_re=re.compile(r'পরিবর্তে')
track3_re=re.compile(r'মেয়াদে|মেয়াদে')
break_re=re.compile(r'হতে')

min_start_re=re.compile(r'অর্থায়নে')
min_start_re_01=re.compile(r'বিভাগের\s*সদস্য|সদস্য')
min_end_re=re.compile(r'আওতাধীন')

planning_div_start_re=re.compile(r'পরিকল্পনা\s*কমিশনের|পরিকল্পনা')
planning_div_end_re=re.compile(r'বিভাগের')

activity_start_re=re.compile(r'তিনি\s*বলেন\s*যে')
activity_start_point_re=re.compile(r'প্রস্তাবিত\s*প্রকল্পটির\s*আওতায়|\((ক|১)\)')
activity_grap_re=re.compile(r'\(\s*ক\s*\)|লক্ষ্যে')
end_activity_re=re.compile(r'করা\s*হবে।|আছে।|সম্পাদন\s*করা।')
benefite_start_re=re.compile(r'তিনি\s*আরও\s*বলেন\s*যে')
benefite_start_re01=re.compile(r'(প্রস্তাবিত|প্র্রস্তাবিত)\s*প্রকল্পটি\s*বাস্তবায়িত\s*হলে')
benefite_end_re=re.compile(r'হবে।|ভূমিকা\s*রাখবে।')

##Ministry project extraction rules
div_start=re.compile(r'বিভাগ:|বিভাগ')
project_start=re.compile(r'(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)?(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d).')
date_mid_point=re.compile(r'হতে')
ministry=re.compile(r'মন্ত্রণালয়|অধিদপ্তর')
min_estimated_cost=re.compile(r'প্রকল্প\s*ব্যয়|প্রকল্প\s*ব্যয়:')
taka=re.compile('টাকা')
date_format_re=re.compile(r'(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)\s*(-|/|.)\s*(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)\s*(-|/|.)\s*(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)')
year_re=re.compile(r'\d\d\d\d|(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)(০|১|২|৩|৪|৫|৬|৭|৮|৯|\d)')




