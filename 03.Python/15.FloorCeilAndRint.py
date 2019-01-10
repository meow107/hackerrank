# floor
# The floor of x is the largest integer i where i <= x

# ceil
# The ceiling of x is smallest integer i where i >= x

# rint
# The rint tool rounds to the nearest integer of input element-wise

import numpy

array = list(map(float, input().split()))

array = numpy.array(array)

print (numpy.floor(array))
print (numpy.ceil(array))
print (numpy.rint(array))