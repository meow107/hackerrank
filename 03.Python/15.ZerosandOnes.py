# zeros
# import numpy

# print (numpy.zeros((1, 2)))

# print (numpy.zeros((1, 2), dtype = numpy.int))

# ones
# import numpy

# print (numpy.ones((1, 2)))
# print (numpy.ones((1, 2), dtype = numpy.int))

import numpy

list_i = list(map(int,input().split()))

print(numpy.zeros(list_i, dtype = numpy.int))
print(numpy.ones(list_i, dtype = numpy.int))

