#Beautiful Days at the Movies
import sys

# 20 23 6
# Sample Output

# 2

# i = 20
# j = 23 
# k = 6

i, j, k = input().strip().split(' ')
i, j, k = [int(i), int(j), int(k)]

day = i
beautiful_day_counter = 0
while day <= j:
    reverse_day = int (str(day)[::-1])
    distance = abs(day - reverse_day)

    if distance % k == 0:
        beautiful_day_counter += 1
    day += 1
print (beautiful_day_counter)