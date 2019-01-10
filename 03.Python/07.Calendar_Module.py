# input
# 08 05 2015

# output
# WEDNESDAY

import calendar

M, D, Y =  input().split()
M, D, Y =  int(M), int (D), int(Y)
day_name = str(calendar.day_name[calendar.weekday(Y,M,D)])

print (day_name.upper())

