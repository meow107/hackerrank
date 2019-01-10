# input 
# 2
# 6
# 4 3 2 1 3 4
# 3
# 1 3 

# output
# Yes
# No

# Way 1:
for _ in range(int(input())):
    l = input() == 0 or list(map(int, input().split()))
    i = l.index(min(l))
    print('l')
    print(l)
    print("l[:i]")
    print(l[:i])
    print("sorted(l[:i]")
    print(sorted(l[:i],reverse=True))
    print("l[i:]")
    print(l[i:])
    print("sorted(l[i:])")
    print(sorted(l[i:]))
    # print("Yes" if l[:i] == sorted(l[:i],reverse=True) and l[i:] == sorted(l[i:]) else "No")

# Way 2
# from collections import deque

# for _ in range(int(input())):  
#     _, queue =input(), deque(map(int, input().split()))

#     print ("queue")
#     print(queue)

#     queue = sorted(queue)
    
#     print ("reversed queue")
#     print(queue)
#     for cube in reversed(queue):
#         if queue[-1] == cube:
#              queue.pop()
#         elif queue[0] == cube:
#              queue.popleft()
#         else:
#             print('No')
#             break
#     else: print('Yes')
            

