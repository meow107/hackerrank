#Sock Merchant
import sys


# n = int(input().strip())
# c = [int(c_temp) for c_temp in input().strip().split(' ')]

n = 9
c = [10, 20, 20, 10, 10, 30, 50, 10, 20]
#c = [10,10]
#c = [10,10,20,30,40,50]

pairs = 0

# have 2 elements
if len(c) == 2:
    if  c[1] == c[0]:
        pairs = 1
elif len(c) <= 1:
    pairs = 0
else:
    distinct_list = list(set(c))
    for item in distinct_list:
        count_time = 0
        for c_time in c:
            if c_time == item :
                count_time += 1
        if count_time >= 2 :
            pairs += int(count_time  / 2)
    
print (pairs)
        

