# input
# 1 4
# x**3 + x**2 + x + 1

# output
# True
x, k = input().split()
k = int(k)
s = str(input())

s = s.replace('x', x)
if k == eval(s):
    print(True)
else:
    print(False)


