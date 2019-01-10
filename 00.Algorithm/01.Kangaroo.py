#Kangaroo
# X1 + (V1 * N) = X2 + (V2 * N)
#<=> N = (X1 - X2) / (V2 - V1)
# X1 != X2 && V2 != V1 & (X1 - X2) % (V2 - V1) & N > 0


#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]


if (x1 != x2) and (v1 != v2) :
    N = (x1 - x2) /  (v2 - v1)
    surplus = (x1 - x2) % (v2 - v1)
    if (N > 0 ) and (surplus == 0) :
        print ("YES")
    else:
        print("NO")
else:
    print("NO")