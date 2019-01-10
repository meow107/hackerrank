#unsorted = [6,31415926535897932384626433832795,1,3,10,3,5]
#out 
# 1
# 3
# 3
# 5
# 10
# 31415926535897932384626433832795

import sys

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)

unsorted.sort(key=int)
for item in unsorted:
    print (item)

