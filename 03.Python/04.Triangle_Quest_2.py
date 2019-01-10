# Demlo Number
# https://archive.lib.msu.edu/crcmath/math/math/d/d114.htm

# input
# 5

# output
# 1
# 121
# 12321
# 1234321
# 123454321

# from
# 1 ^ 2
# 11 ^ 2
# 111 ^ 2
# 1111 ^ 2
# 11111 ^ 2 

for i in range(1, int(input()) + 1):
     print( (10 ** i // 9) ** 2 )

