# input
# 4 
# a a c d
# 2

# output
# 0.8333

# 1
# b
# 1
# 0.000000000000

from itertools import combinations

n = (int)(input())
s = list(map(str, input().split()))
k = (int)(input())

s = sorted(s)
combanations_list = list(combinations(s, k))
rate = 0.0
for item in combanations_list:
    
    if item[0] == 'a' or item[k - 1] == 'a':
        rate += 1
rate =  rate/ (float)(len(combanations_list))
        

print (rate)



