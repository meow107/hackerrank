# input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# output 
# 8

n_english_subscribes = (int)(input())
english_subscribes = set(map(int, input().split()))

n_french_subscribes = (int)(input())
french_subscribes = set(map(int, input().split()))


# symmetric_differences = english_subscribes.symmetric_difference(french_subscribes)
# or
symmetric_differences = english_subscribes ^ french_subscribes
print (len(symmetric_differences))