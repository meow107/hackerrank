
# SOSSPSSQSSOR
# 3
#S = "SOSSPSSQSSOR"
import sys

S = input().strip()
sos = "SOS"
standard_sos = ""

n_s = len(S)
loops = n_s / 3
while loops >= 0:
    standard_sos +=  sos
    loops -= 1
count_difference = 0
for index in range(n_s):
    if standard_sos[index] != S[index]:
        count_difference += 1 
print (count_difference)


