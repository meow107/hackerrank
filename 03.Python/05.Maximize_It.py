# input
# 3 1000
# 2 5 4
# 3 7 8 9 
# 5 5 7 8 9 10 

# 7 952
# 6 386364143 56297585 479292050 782778989 177771725 945191156
# 7 458982242 957774948 25202756 357554307 248513713 506622954 769577156
# 3 109432676 494972174 914814315
# 1 49979276
# 2 491584479 103564062
# 1 25883738
# 1 460971693

# 943

#output
# 206
from itertools import product

K , N = input().split()
K , N = int(K), int(N)
i = 0
all_members = []
while i < K:
    line = list(map(int, input().split()))
    # The fist number in every line is number of list.So we need to get from the element which index equals 1
    all_members.append(line[1:])
    i += 1

max_fx = - 1
n_lines = len(all_members)
list_combinatioms = list(product(*all_members))

for combination in list_combinatioms:
    n_combination = len(combination)

    # Counting sum
    #sum_combination = 0
    # for item in combination:
    #     sum_combination += item ** 2
    # sum_combination = sum_combination % N
   
    # counting sum with other way
    sum_combination = sum([x**2 for x in combination]) % N
    max_fx = max(max_fx, sum_combination)
        
print (max_fx)