import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
i = n - 1
reversed_str = ""
while i > - 1 :
    str_item = ""
    if i == n - 1:
        str_item += str(arr[i])
    else:
        str_item += (" " + str(arr[i]))
        
    
    reversed_str += str_item
    i -= 1

print (reversed_str)