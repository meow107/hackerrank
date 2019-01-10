### shape
# #a. Using shape to get array dimensions
# import numpy
# my_1D_array = numpy.array([1, 2, 3, 4, 5])
# print (my_1D_array.shape)

# my_2D_array = numpy.array([[1, 2] ,[3, 4], [6, 5]])
# print (my_2D_array.shape)

# #b. Using shape to change array dimensions
# import numpy

# change_array = numpy.array([1,2,3,4,5,6])
# change_array.shape = (3, 2)
# print (change_array)

### reshape
# import numpy

# my_array = numpy.array([1, 2, 3, 4, 5, 6])
# print (numpy.reshape(my_array, (3,2)))


import numpy

array = list(map(int, input().split()))
print(numpy.reshape(array, (3,3)))

# array = input().strip().split(' ')
# print(numpy.array(numpy.reshape(array, (3,3)),int))