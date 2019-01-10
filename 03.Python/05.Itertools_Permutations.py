from itertools import permutations

s,k = input().split()
k = int(k)
permutations_list =  list(permutations(list(s),k))
for index, item in enumerate(permutations_list):
    permutations_list[index] = ''.join(item)
permutations_list.sort()
print(*permutations_list, sep = '\n')

