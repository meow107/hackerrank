from collections import OrderedDict, Counter
from operator import itemgetter


s = input().strip()

d = OrderedDict(Counter(s))
d = OrderedDict(sorted(d.items(), key = itemgetter(0)))
d = sorted(d.items(), key = itemgetter(1), reverse=True)

for item in d[:3]:
    print ("%s %d" %(item[0], item[1]))
 
