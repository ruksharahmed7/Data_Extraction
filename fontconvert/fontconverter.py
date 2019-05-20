from bijoy2unicode import converter
test = converter.Unicode()
import  re
import config as configfile
import dataExtraction.fontconvert.bijoy_to_unicode as bijoy_to_unicode
check_ascii_re=re.compile(r'[a-z]K|Rvbyqvwi|A‡±vei|wmGgGmwW|GmGm|mfvcwZ|Uvt|Revew|mwPe|'
                          r'Nbwgt|Lyjbv|cvZv|welqvejx|fvov|PvjK|AwWUwiqvg|mnKvix|mnvqK|'
                          r'Avmb|evRvi|mgRvZxq|:wg|XvKv|cyKyi|GmGmwm|PvjK|wnmve|mnvqK|'
                          r'GKi|GKiXvKv|fvZv|evwo|fvZvw|cwigvY|BKbwgK|wefvM|wWwcwc|evsjv|'
                          r'myweavw|kniv|UvKv|wmwbqi|jvj|Kgjv|meyR|weeiY|Ntwgt|mvj|ZvwiL|'
                          r'ewikvj|wRIwe|wbR|nvqvwis|exgv|wU|Rvgvjcyi|gqgbwmsn|wbKjx|Ryb|'
                          r'cvwb|RyjvB|Aby|Drm|aiY|FY|GKK|Pjgvb|cwigvb|Rxc|wKtwgt|Bbcy|'
                          r'UvsMvBj|bvMicyi|KvwjnvZx|gaycyi|NvUvBj|evmvBj|‡kicyi|†Rjvi')


def bijoy2uni(s):
    try:
        #print(s)
        c = s.encode('ascii', 'replace')
        #print(c)
        d=c.decode('utf-8')
        #print(d)
        cnt=d.count('?')
        #print(cnt)
        #print(len(s))
        l=len(s)
        percentage=(cnt/l)*100
        #print(percentage)
        if(percentage>configfile.Threshold['font_conversion_low'] and percentage<configfile.Threshold['font_conversion_high']):
            toUnicode = test.convertBijoyToUnicode(s)
            #toUnicode = bijoy_to_unicode.convertBijoyToUnicode(s)
            #print(toUnicode)
            return toUnicode
        elif(not (check_ascii_re.search(s)==None) and cnt==0):
            toUnicode = test.convertBijoyToUnicode(s)
            #toUnicode = bijoy_to_unicode.convertBijoyToUnicode(s)
            #print(toUnicode)
            return toUnicode
        else:
            #print(s)
            return s
    except IndexError:
        #print('error:'+s)
        toUnicode = bijoy_to_unicode.convertBijoyToUnicode(s)
        #print(toUnicode)
        return toUnicode