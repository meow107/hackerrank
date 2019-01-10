# Birthday Cake Candles

import sys

n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
last_index = len(height) - 1
#print (height)

height.sort()

max_value = height[last_index]
count = 0
for item in height :
    if item == max_value:
        count += 1
print(count)