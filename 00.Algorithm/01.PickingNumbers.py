# n = int(input().strip())
# a = [int(a_temp) for a_temp in input().strip().split(' ')]
n = 6
#n = 100
#a = [4,6,5,3,3,1]
a = [1,1,2,2,2,3]

#a =  [4,97,5,97,97,4,97,4,97,97,97,97,4,4, 5, 5, 97 ,5, 97 ,99 ,4 ,97 ,5, 97, 97 ,97 ,5 ,5 ,97, 4 ,5 ,97 ,97 ,5, 97 ,4 ,97, 5 ,4, 4, 97, 5, 5 ,5 ,4 ,97, 97, 4 ,97 ,5 ,4, 4, 97, 97, 97, 5 ,5 ,97 ,4 ,97 ,97 ,5, 4 ,97 ,97 ,4 ,97 ,97, 97 ,5 ,4 ,4, 97, 4 ,4 ,97 ,5 ,97 ,97 ,97 ,97 ,4, 97, 5, 97, 5, 4, 97, 4, 5, 97, 97, 5, 97, 5, 97, 5, 97, 97, 97]
a.sort()
steps = 0
max_steps = 0
previous_item = a[0]
min_item = a[0]

for i in range(0, n):
    deta_a = a[i] - previous_item 
    if deta_a <= 1 and abs(min_item - a[i]) <= 1:
        steps += 1
        if a[i] < min_item:
            min_item = a[i]
    else:
        steps = 1
        min_item = a[i]
    if steps > max_steps:
        max_steps = steps
    previous_item = a[i]
print (max_steps)