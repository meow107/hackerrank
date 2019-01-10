v = (int)(input().strip())
n = (int)(input().strip())
array =  [int(tmp) for tmp in input().strip().split(' ')]

array.sort()
for index, item in enumerate(array):
    if v == item:
        print (index)
        break

