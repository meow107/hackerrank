
import sys

# d1 = 9
# m1 = 6 
# y1 = 2015
# d2 = 6
# m2 = 6
# y2 = 2015
#out = 45

# d1 = 28
# m1 = 2 
# y1 = 2015
# d2 = 15
# m2 = 4
# y2 = 2015
# # out = 0


d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

fine = 0

if y1 <y2 :
    pass
elif y1 == y2:
    if m1 < m2:
        pass
    elif m1 == m2:
        if d1 > d2:
            fine =  15 * (d1 - d2)
    else:
        fine = 500 * (m1 - m2)
else:
    fine = 10000
    

print(fine)








