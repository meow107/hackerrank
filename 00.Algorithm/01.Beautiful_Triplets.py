# 7 3
# a =[1, 2, 4, 5, 7, 8, 10]

# d =  3
# n = 7

n,d = input().strip().split(' ')
n,d = [int(n),int(d)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

#item in a : Check item in "a" array.
count = 0
for item in a:
    if item + d in a and item + 2 * d in a:
        count += 1
print(count)