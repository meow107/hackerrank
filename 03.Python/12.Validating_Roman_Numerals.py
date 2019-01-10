# CDXXI

# From : http://www.diveintopython3.net/regular-expressions.html
# Sometimes , I feel so stupid.


import re

s = input()
isRomanNumeral = True
patern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
m = re.search(r'%s' % patern, s)
print (bool(m))
        
