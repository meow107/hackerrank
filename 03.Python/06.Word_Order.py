# input
# 4
# bcdef
# abcdefg
# bcde
# bcdef

# output
# 3
# 2 1 1

from collections import OrderedDict

# Should use OrderedDict to keep the order.

d = OrderedDict()
n = int(input())
for i in range(n):
    key = input()
    if key not in d.keys():
        d[key] = '1'
    else:
        counter = int(d[key])
        counter += 1
        d[key] = str(counter)
print(len(d.keys()))
print (' '.join(d.values()))

        
