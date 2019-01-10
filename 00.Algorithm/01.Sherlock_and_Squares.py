
# Sherlock and Squares

import sys
import math


# Watson gives two integers ( and ) to Sherlock and asks if he can count the number of square integers between  and  (both inclusive).

# Note: A square integer is an integer which is the square of any integer. For example, 1, 4, 9, and 16 are some of the square integers as they are squares of 1, 2, 3, and 4, respectively.


def count_square_number(min_value, max_value):
    
    # Ha Ha this is a magical code.
    min_root_square = math.ceil(sqrt(min_value))
    max_root_square = math.ceil(sqrt(max_value))

    return max_root_square - min_root_square

n = int(input().strip())
for i in range (0, n):
    min_value, max_value = input().strip().split(" ")
    min_value, max_value = (int)(min_value), (int)(max_value)
    max_value += 1
    print (count_square_number(min_value,max_value))