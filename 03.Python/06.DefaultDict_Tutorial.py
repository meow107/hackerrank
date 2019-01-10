# input
# 5 2
# a
# a
# b
# a
# b
# a
# b

# output
# 1 2 4
# 3 5

from collections import defaultdict

n, m = input().split()
n, m = int(n), int(m)
d = defaultdict(list)

for i in range (1, n + 1):
    d[input()].append(str(i))

for i in range (m):
    print(' '.join(d[input()]) or - 1)
    

