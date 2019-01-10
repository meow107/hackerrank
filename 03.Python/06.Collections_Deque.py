# input
# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# output
# 1 2

from collections import deque

# append, pop, popleft and appendleft
n = int(input())
d = deque()
for i in range(n):
    comand = input()
    if comand == "pop":
        d.pop()
    elif comand == "popleft":
        d.popleft()    
    else:
        comand, item = comand.split()
        if comand == "append":
            d.append(str(item))
        else:
            d.appendleft(str(item))
print(' '.join(d))