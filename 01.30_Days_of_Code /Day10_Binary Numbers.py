#!/bin/python3

#Day10_Binary Numbers

import sys

n = int(input().strip())
base_2 = "{0:b}".format(n)

count_1 = 0
max_count1 = 0
for digit in base_2:
    if digit == "1":
        count_1 +=1
    else:
        max_count1 = max(count_1,max_count1)
        count_1 = 0
if count_1 > 0:
    max_count1 = max(count_1, max_count1)

print (max_count1)

