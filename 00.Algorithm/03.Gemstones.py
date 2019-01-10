import sys

def gemstones(arr):
    set_array = set(arr[0])
    len_array = len(arr)
    if len_array > 1:
        for i in range (1, len_array):
            set_array = set_array.intersection(set(arr[i]))
    return len(set_array)

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
   arr_t = str(input().strip())
   arr.append(arr_t)
result = gemstones(arr)
print(result)

