from itertools import combinations

def print_combination(s, i):
    s = sorted(s)
    combination_list = list(combinations(s, i))
    for index, item in enumerate(combination_list):
        print(''.join(item))

s, k = input().split()
k = (int)(k) 

for i in range(1, k + 1):
    print_combination(s, i)
    

    






