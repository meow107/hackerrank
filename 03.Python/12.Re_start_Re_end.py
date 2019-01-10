# Notes: 
# Problem : finditer not contains overllaped index 
# Solve in regex patern we have ?= , that means "getting matches with overllap indexs"

import re

s = input()
k = input()

break_signal = False
if len(s) >= len(k):
    matches = list(re.finditer(r'(?=(%s))' % k, s))
    if matches:
        for match in matches:
            print("(%d, %d)" %(match.start(1), match.end(1) -  1))
    else:
        break_signal = True       
else:
    break_signal = True

if break_signal == True:
    print((-1, -1))

