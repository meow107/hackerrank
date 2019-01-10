# Hint : https://stackoverflow.com/questions/32169040/replace-with-and-using-re-sub-in-python
# (?<= ) ... (?= )

import re

def replace_s(s):
    s = re.sub(r'(?<= )\&\&(?= )', "and", s)
    s = re.sub(r'(?<= )\|\|(?= )', "or", s)
    return s
    
N = int(input())
for i in range(N):
    s = input()
    if len(s) == 0 :
        print ("")
    else :
        print(replace_s(s))
        