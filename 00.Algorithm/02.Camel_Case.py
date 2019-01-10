# in : saveChangesInTheEditor
# out : 5

import sys
import string

#s = input().strip()

s = "saveChangesInTheEditor"
count_word = 1
for item in s:
    if item == item.upper():
        count_word += 1
print(count_word)

