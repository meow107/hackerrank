# input
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 1 2 3

# output
# False

A = set(map(int, input().split()))
n = (int)(input())
i = 0
is_totally_supper = False
while i < n:
    B = set(map(int, input().split()))
    lenA = len(A)
    lenB = len(B)
    if lenA > lenB:
        if B - A == set():
            is_totally_supper = True
        else:
            is_totally_supper = False
            break
    else:
        is_totally_supper = False
        break
    i += 1
print(is_totally_supper)

# With test case file
# file = open("strict_superset.rtf","r")
# lines = file.readlines()

# A = set(map(int, lines[0].split(" ")))
# n = (int)(lines[1])

# i = 0
# is_totally_supper = False

# lenA = len(A)

# while i < n:
#     B = set(map(int, lines[2 + i].split()))
#     lenB = len(B)
   
#     if lenA > lenB:
#         if A & B == B:
#             is_totally_supper = True
#         else:
#             is_totally_supper = False
#             break
#     elif lenA < lenB:
#        is_totally_supper = False
#        break
#     print (is_totally_supper)
#     i += 1
# print(is_totally_supper)