# 3 2
# 1 5 3
# 3 1
# 5 7

# 1

n, m = map(int,input().split())
array = list(map(int, input().split()))
A = set (map(int, input().split()))
B = set (map(int, input().split()))

total = 0
for item in array:
    if item in A:
        total += 1
    elif item in B:
        total -= 1
print(total)

# Other way
# total = sum([(i in A) - (i in B) for i in array])
# print(total)