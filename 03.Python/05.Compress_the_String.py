from itertools import groupby
s = input()

groupby_list = groupby(s)

result =  ""
for key,item in groupby_list:
    result += str.format("(%d, %s) " % (len(list(item)), key))
print(result)

