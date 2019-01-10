# intput
# 5
# 12 9 61 5 14 

# output
# True

n = (int)(input())
list_ = list (map(int,input().split()))
print (True if all([x > 0 for x in list_]) and any([str(x) == str(x)[::-1] for x in list_])  else False)



