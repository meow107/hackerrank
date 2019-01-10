#Angry Professor

# import sys

# t = int(input().strip())
# for a0 in range(t):
#     n,k = input().strip().split(' ')
#     n,k = [int(n),int(k)]
#     a = [int(a_temp) for a_temp in input().strip().split(' ')]

def make_decision(n,k,a):
    arrival_person = 0
    for item in a :
        if item <= 0:
            arrival_person += 1
    if arrival_person >= k:
        print("NO")
    else:
        print ("YES")

n = 4
k = 3
a = [-1,-3,4,2]

# n = 4
# k = 2
# a = [0,-1,2,1]

make_decision(n,k,a)

