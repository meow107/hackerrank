from itertools import combinations_with_replacement

s, k = input().split()
k = (int)(k)

s = sorted(s)
com_re = list(combinations_with_replacement(s, k))

for item in com_re:
    print(''.join(item))



