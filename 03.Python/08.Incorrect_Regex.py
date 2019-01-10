# input
# 2
# .*\+
# .*+

# output
# True
# False

import re

n = int(input())
for i in range(n):
    s = input()
    try:
        re.compile(s)
        print(True)
    except re.error as e:
        print(False)
