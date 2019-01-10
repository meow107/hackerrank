# input
# n = 4
# set_a = {2, 4, 5, 9}
# m = 4
# set_b = {2, 4, 11, 12}

# output
# 5
# 9
# 11
# 12

n = (int)(input())
set_a_in = input().split()
m = (int)(input())
set_b_in = input().split()

set_a = set(list(map(int, set_a_in)))
set_b = set(list(map(int, set_b_in)))

set_a_not_b = set_a.difference(set_b)
set_b_not_a = set_b.difference(set_a)

union_all = set_a_not_b.union(set_b_not_a)
union_all = sorted(union_all)

for item in union_all:
    print (item)
