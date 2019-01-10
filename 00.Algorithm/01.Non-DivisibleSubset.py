n,k = input().strip().split()
n, k = int(n), int(k)

a = list(map(int, input().split()))

L = [0]*k

print(L)

for x in a: 
    L[x % k] += 1

print(L)

res = 0
for i in range(k//2+1):
    if i == 0 or k == i*2:
        res += bool(L[i])
    else:
        res += max(L[i], L[k-i])

print(res)

# 4 3
# 1 7 2 4

# 6 9
# 422346306 940894801 696810740 862741861 85835055 313720373

# 5