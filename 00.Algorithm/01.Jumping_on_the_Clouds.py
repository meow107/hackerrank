# Jumping on the Clouds

# n = 7
# c = [0 ,0 ,1 ,0 ,0 ,1, 0]
# output = 4

# n = 6
# c = [0 ,0 ,0, 0 ,1 ,0]
# output = 3

import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

count = 0
index = 0
while index < len(c):
    count += 1
    next_index = index + 2
    if next_index < len(c):
        if c[next_index] != 1:
            index += 2
        else:
            index += 1
    else:
        index += 1
    
    
print(count - 1)