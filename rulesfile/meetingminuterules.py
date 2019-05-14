import re

decision_re=re.compile(r'সিদ্বান্ত|সিদ্ধান্তঃ|সিদ্ধান্ত:|সিদ্ধান্ত')
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
