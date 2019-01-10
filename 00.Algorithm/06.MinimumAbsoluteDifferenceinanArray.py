# n = 3
# a = [3, -7, 0]

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

a.sort()
i = 1
min_absolute = abs(a[0] - a [1])
while i < n - 1:
    min_absolute = min(min_absolute, abs(a[i] - a[i + 1]))
    i += 1
print (min_absolute)

