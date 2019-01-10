import re

s = input()
m = re.search(r"([A-Z0-9a-z])\1+", s)
print(m.group(1) if m else -1)
    
    

