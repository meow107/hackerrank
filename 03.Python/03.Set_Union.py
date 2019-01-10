# input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# ouput
# 13
n_english_subscribes = (int)(input())
english_subscribes = set(map(int, input().split()))

n_french_subscribes = (int)(input())
french_subscribes = set(map(int, input().split()))

union_all = english_subscribes | french_subscribes 
# or
# union_all = english_subscribes.union(french_subscribes)
# is the same


print(len(union_all))



