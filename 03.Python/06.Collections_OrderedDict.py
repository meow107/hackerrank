# input
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30

# output
# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20

from collections import OrderedDict

n = int(input())
d = OrderedDict()

for i in range(n) :
    in_ =  str(input())
    price = ''.join((filter(str.isdigit,in_)))
    key = in_.replace(price,'')

    if key not in d.keys():
        d[key] = int(price)
    else:
        sum_price = d[key]
        d[key] = int(sum_price) + int(price)
        
for item in d.items():
    print("%s%d" %(item[0], item[1]))
