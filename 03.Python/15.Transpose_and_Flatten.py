# Transpose
# Changed dimension of array
# import numpy

# my_array = numpy.array([[1, 2, 3], [4, 5, 6]])
# print(numpy.transpose(my_array))

# Flatten
# a copy of the input array flattened to one dimension
# import numpy

# my_array = numpy.array([[1,2,3],[4,5,6]])

# print(my_array.flatten())

import numpy

row, column = input().split()
row, column = int(row), int(column)
array = []

for i in range(row):
    row_array = list(map(int, input().split()))
    array.append(row_array)

array = numpy.array(array)

print (numpy.transpose(array))
print (array.flatten())


    
