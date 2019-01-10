# import numpy

# print(numpy.identity(3))

#import numpy
# print(numpy.eye(8, 8, k = 1))
# print ("-------------------------")
# print(numpy.eye(8, 8, k = 0))
# print ("-------------------------")
# print ("-------------------------")
# print (numpy.eye(8, 8, k = -1))


import numpy

n, m = input().split()
n, m = int(n), int(m)

print (numpy.eye(n, m, k = 0))

