#!/bin/python3

import sys


#n = int(input().strip())
n = 3
i = 0
j = 0
k = n - 1

while i < n : 
    j = 0
    s = ""
    while j < n and k >= 0:
       # print ("j = %d" % (j))
        if j < k :
            s += " "
        else:
            s += "#"
        
        j += 1
    print (s)

    k -= 1
    i += 1
