import numpy

n, m = input().split()
n, m = int(n), int(m)
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    b.append(list(map(int, input().split())))

a, b =  numpy.array(a), numpy.array(b)
print (a + b, a - b, a * b, a//b, a % b, a ** bytearray, sep = '\n' )
