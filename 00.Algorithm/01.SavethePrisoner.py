import sys

def saveThePrisoner(n, m, s):
    # Complete this function
    the_last = s + (m - 1)
    if the_last <= n :
        return the_last
    else:
        return (the_last % n) + 1
         


t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)

