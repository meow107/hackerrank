# min
# returns the minimum value along a given axis

# max 
# returns the maximum value along a given axis

import numpy

n, m = input().split()
n, m = int(n), int(m)

array = [] 
for i in range(n):
    array.append(list(map(int, input().split())))

array = numpy.array(array)
min_array = numpy.min(array, axis = 1)

print (numpy.max(min_array))
