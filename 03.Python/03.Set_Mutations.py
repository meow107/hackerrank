# input
# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11
# update 2
# 55 66
# symmetric_difference_update 5
# 22 7 35 62 58
# difference_update 7
# 11 22 35 55 58 62 66

# output
# 38

n = (int)(input())
elements = set(map(int, input().split()))

n_commands = (int)(input())
i = 0
while i < n_commands:
    command, n_other_elements = input().split()
    other_elements = set(map(int, input().split()))
    if command == "intersection_update":
        elements.intersection_update(other_elements)
    elif command == "update":
        elements.update(other_elements)
    elif command == "symmetric_difference_update":
        elements.symmetric_difference_update(other_elements)
    elif command == "difference_update":
        elements.difference_update(other_elements)
    else:
        pass
    i += 1
print(sum(elements))

