#import numpy

# array_1 = numpy.array([1, 2, 3])
# array_2 = numpy.array([4, 5, 6])
# array_3 = numpy.array([7, 8, 9])

# print(numpy.concatenate((array_1, array_2, array_3)))


# import numpy

# array_1 = numpy.array([[1,2,3], [0,0,0]])
# array_2 = numpy.array([[0,0,0], [7,8,9]])

# print (numpy.concatenate((array_1, array_2), axis = 1))

import numpy

n, m ,p = input().split()
n, m, p = int(n), int(m), int(p)

list_n = []
list_m = []

for i in range(n):
    list_n.append(list(map(int,input().split())))

for i in range(m):
    list_m.append(list(map(int, input().split())))
    
print(numpy.concatenate((list_n, list_m)))