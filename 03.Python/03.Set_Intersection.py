# input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# ouput
# 5

n_english_subscribes = (int)(input())
english_subscribes = set(map(int, input().split()))

n_french_subscribes = (int)(input())
french_subscribes = set(map(int, input().split()))

intersections = english_subscribes.intersection(french_subscribes)
# or 
# intersections = english_subscribes & french_subscribes
# is the same
print (len(intersections))