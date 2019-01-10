#Equalize the Array
import sys

n = input().strip()
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = list(set(a))

count_max = 0
for b_item in b:
    count = 0
    for a_item in a:
        if b_item == a_item:
            count += 1
    count_max = max(count_max,count)
print (len(a) - count_max )
