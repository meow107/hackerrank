# dot tool returns the dot product -> result of a dot product is a number
# reference : https://en.wikipedia.org/wiki/Dot_product


# cross tool returns the cross product -> result of a cross product is a vector
# reference : http://tutorial.math.lamar.edu/Classes/CalcII/CrossProduct.aspx

import numpy

n = int(input())

A = []
B = []

for i in range( 2 * n):
    line = list(map(int, input().split()))
    if i < n :
        A.append(line)
    else:
        B.append(line)

print(numpy.dot(A, B))
