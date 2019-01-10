# Sample Input

# 5
# 2 4 6 8 3
# Sample Output

# 2 4 6 8 8 
# 2 4 6 6 8 
# 2 4 4 6 8 
# 2 3 4 6 8 

import sys

# n = 5
# array =  [2 ,4, 6, 8 ,3]

# n = 14
# array = [1, 3 ,5 ,9 ,13 ,22 ,27, 35, 46 ,51 ,55 ,83, 87 ,23]

# n = 10
# array = [2, 3, 4 ,5 ,6 ,7, 8, 9 ,10 ,1]


n = int(input().strip())
array = [int(temp) for temp in input().strip().split(' ')]

key = array[n - 1]
array.pop()
n -= 1

i = n - 1
stop = False
while i >= 0:
    new_array = array[:]
    if key > array[i]:
        new_array.insert(i + 1,key)
        stop = True
    else:
        new_array.insert(i, array[i])

    print(" ".join(str(x) for x in new_array))
    if stop == True :
        break

    i -= 1

if stop == False:
    array.insert(0,key)
    print(" ".join(str(x) for x in array))


