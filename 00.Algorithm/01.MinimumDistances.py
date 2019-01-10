# A = [7,1 ,3 ,4, 1, 7]
# n = 6 
# Minimum Distances

import sys

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

min_i_j = n

for i in range (0,n -1):
    min_step = n
    for j in range( i +  1, n):
        if i != j and A[i] == A[j]:
            min_i_j = min(abs(i - j), min_i_j)

if min_i_j == n:
    min_i_j = -1
print (min_i_j)