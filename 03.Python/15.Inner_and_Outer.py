# inner product
# returns inner product of two arrays

# outer product
# return the outer product of two arrays

# reference : http://linear.axler.net/InnerProduct.pdf

import numpy

A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))

print (numpy.inner(A, B))
print (numpy.outer(A, B))