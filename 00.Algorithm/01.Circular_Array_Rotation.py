# So slow haha
# Circular Array Rotation
import sys

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

for times in range(0,k):
    last_item = a[len(a) - 1]
    a.insert(0, last_item)
    a.pop()

for a0 in range(q):
    m = int(input().strip())
    print (a[m])