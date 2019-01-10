# sum
# returns the sum of array elements over a given axis

# prod
# return product of array elements over a given axis -> product element A * element B

import numpy

n, m = input().split()
n, m = int(n), int(m)
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
sum_array = numpy.sum(array, axis = 0)
product_array = numpy.prod(sum_array)
print (product_array)