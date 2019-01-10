#BonAppeti
import sys

# From File
# f = open('input04.txt', 'r')
# a = []
# for item in f:
#     line = item.rstrip('\n')
#     a.append(line)
 
# n, k = a[0].strip().split(' ')
# n, k = [int(n), int(k)]
# charges = list(map(int, a[1].strip().split(' ')))
# b_charge = int(a[len(a) -1].strip())

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
charges = list(map(int, input().strip().split(' ')))
b_charge = int(input().strip())

b_actual = 0
for index in range(0, len(charges)):
    if index != k :
         b_actual += charges[index]
b_actual = (int)(b_actual / 2)
if b_actual == b_charge:
    print ("Bon Appetit") 
else:
    print (abs(b_charge - b_actual))

        

