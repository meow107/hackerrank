#Electronics Shop
import sys 

#539854

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    max_money = -1
    for keyboard in keyboards:
        for drive in drives:
            price = keyboard + drive
            if price <= s:
                max_money = max(max_money, price)
    return max_money
                

# s = 11
# n = 2
# m = 3
# keyboards = [3]
# drives = [5,2,8]
# From file 
f = open('electronics_shop.txt')
a = []
for item in f: 
    line = item.rstrip('\n')
    a.append(line)
s , n, m = a[0].strip().split(' ')
s, n, m = [int(s), int(n), int(m)]
keyboards = list(map(int, a[1].strip().split(' ')))
drives = list(map(int, a[2].strip().split(' ')))



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


moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)


