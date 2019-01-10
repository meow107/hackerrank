# arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0 ,0 ,2, 4, 4 ,0], [0, 0 ,0 ,2 ,0 ,0],[0 ,0 ,1, 2 ,4 ,0]]
# out = 19

#arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,9,2,-4,-4,0],[0,0,0,-2,0,0],[0,0,-1,-2,-4,0]]
#out : 13

#arr = [[0,-4,-6,0,-7,-6],[-1,-2,-6,-8,-3,-1],[-8,-4,-2,-8,-8,-6],[-3,-1,-2,-5,-7,-4],[-3,-5,-3,-6,-6,-6],[-3,-6,0,-8,-6,-7]]
# out : -19

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
    
n = 6
max_sum = -9 * 7 - 1
for row in range (n - 1):
    for column in range(n - 1):
        previous_row = row -  1
        next_row = row + 1

        previous_column = column - 1
        next_column = column + 1

        if previous_row >= 0 and next_row <= n - 1 and previous_column >= 0 and next_column <= n - 1:
            sum_hour_glass = arr[row][column] + arr[previous_row][previous_column] + arr[previous_row][column] + arr[previous_row][next_column] + arr[next_row][previous_column] + arr[next_row][column] + arr[next_row][next_column]
            max_sum = max(sum_hour_glass, max_sum)
        
print(max_sum)
         








