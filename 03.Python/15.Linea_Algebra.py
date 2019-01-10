# linalg.det
# computes the determinant of an array
# reference : https://www.mathsisfun.com/algebra/matrix-determinant.html

import numpy

n = int(input())
array = []

for i in range(n):
    array.append(list(map(float, input().split())))

print (numpy.linalg.det(array))