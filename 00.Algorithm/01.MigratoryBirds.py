#Migratory Birds

import sys
n = 6
types = [1,4,4,4,5,3]


unique_list = set(types)
max_count = 0
max_type = types[0]
for unique_item in unique_list:
    count = 0
    for type_item in types:
        if unique_item == type_item:
            count += 1
    if count > max_count:
        max_count = count
        max_type = unique_item
    
print (max_type)
    

