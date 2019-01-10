#Cut the sticks
import sys

# n = 6
# arr = [5, 4, 4, 2, 2, 8]
removed_index = []

while len(arr) > 0:
    arr.sort()
    min_value = arr[0]
    removed_index.append(0)
    arr[0] = arr[0] - min_value
    for index in range(1,len(arr)):
        arr[index] = arr[index] -  min_value
        if arr[index] <= 0 :
            removed_index.append(index)

    print (len(arr))
    # https://stackoverflow.com/questions/18837607/remove-multiple-items-from-list-in-python
    arr = [v for i, v in enumerate(arr) if i not in removed_index]
    removed_index = []

