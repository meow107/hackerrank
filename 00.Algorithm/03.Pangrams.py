import re

s = input()
s = (str(s)).upper()
p = r'[^A-Z]'
s = re.sub(p, '', s)
set_s = set(s)
if len(set_s) == 26:
    print("pangram")
else:
    print("not pangram")
