# mean
# computes the arithmetic mean along the specified axis.

# var
# computes the arithmetic variance along the specified axis
# reference : http://www.macroption.com/calculate-variance-standard-deviation-4-steps/

#std 
# computes the arithmetic standard deviation along specified axis.
# reference : https://www.khanacademy.org/math/probability/data-distributions-a1/summarizing-spread-distributions/a/calculating-standard-deviation-step-by-step

import numpy

n, m = input().split()
n, m = int(n), int(m)

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

array = numpy.array(array)

print (numpy.mean(array, axis =  1))
print (numpy.var(array, axis = 0))
print (numpy.std(array))
