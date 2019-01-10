 
 # input
 # 1+2j
 
 # output
 # 2.23606797749979 
 # 1.1071487177940904

import cmath

sequence = str(input())
sequence = sequence.replace(" ", "")
sequence = complex(sequence)
r, phi = cmath.polar(sequence)

print (r)
print (phi)



