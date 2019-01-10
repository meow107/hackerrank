#Arrays - DS
import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

str_arr =  ""

i = n - 1 
while i >= 0:
    if i == 0 :
        str_arr += str(arr[i])
    else :
        str_arr += str(arr[i]) + " "
    i -= 1
print(str_arr)

