#CavityMap

# n = 4
# grid = ["1112","1912","1892","1234"]

# From file
# f = open("cavity.txt","r")
# a = []
# for item in f: 
#     line = item.rstrip('\n')
#     a.append(line)


# n = (int)(a[0])
# print(n)
# grid = []

# for i in range(1,n + 1):
#    grid.append(a[i])


import sys


n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
   grid_t = str(input().strip())
   grid.append(grid_t)
    
output_grid = grid[:]
for row in range(n):
        for column in range(n):
            current_item = (int)(grid[row][column])

            previous_row = row - 1
            previous_column = column - 1

            next_row = row + 1
            next_column = column + 1

            #print("next_row = %d pre row = %d pre colum = %d next row = %d next column = %d"%(next_row,previous_row,previous_column,next_row,next_column))

            top_item = -1
            down_item = -1
            left_item = -1
            right_item = -1
            # top
            if previous_row >= 0 :
                top_item = (int) (grid[previous_row][column])
            # down
            if next_row < n:
                down_item = (int) (grid[next_row][column])
            # left
            if previous_column >= 0:
                left_item = (int)(grid[row][previous_column])
            # right
            if next_column < n:
                right_item = (int)(grid[row][next_column])
            
            if top_item != -1 and down_item != -1 and left_item != -1 and right_item != -1:
                if current_item > top_item and current_item > down_item and current_item > left_item and current_item > right_item:
                    
                    i = 0 
                    len_row = len(output_grid[row])
                    temp_row = output_grid[row]
                    temp_row = temp_row[:column] + "X" + temp_row[column + 1:]
                   
                    output_grid[row] = temp_row

for item in output_grid:
    print (item)

