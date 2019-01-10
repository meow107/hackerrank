import re

# number in range of (100000 - 999999)
# must not contain more than one alternating repetitive digit pair. 
# Alternating repetitive digits are digits which repeat immediately after the next digit. 
# In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.


# https://stackoverflow.com/questions/34573648/finding-all-occurrences-of-alternating-digits-using-regular-expressions

import re

s = input()

pattern_repeat = r'(?=((\d)\d\2))'
pattern_range =  r'^[1-9][\d]{5}$'

repeated_matches = re.findall(pattern_repeat, s)
range_matches = re.match(pattern_range,s)

repeated_condition = len(repeated_matches) < 2
range_condition = bool(range_matches)

print (repeated_condition and range_condition)




    
    






