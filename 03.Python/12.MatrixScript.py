#!/bin/python3

import sys
import re

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
for matrix_i in range(n):
    matrix_t = str(input())
    matrix.append(matrix_t)

print(matrix)
line = ""
for i in range(m):
    for item in matrix:
        item = str(item)
        print (item)
        line += i < len(item) and item[i] or " "

pattern = r'(?<=\w)[!@#$%&\s]+(?=\w)'
print (re.sub(pattern,' ',line))


# 7 3
# Tsi
# h%x
# i #
# sM 
# $a 
# #t%
# ir!

# Test case 6

# 2 2
# # 
#  @

# #  @