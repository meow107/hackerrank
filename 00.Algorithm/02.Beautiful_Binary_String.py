import sys
import re

def minSteps(n, B):
    # Complete this function
    patern = r'010'
    matches = re.findall(patern, B)
    return len(matches)


n = int(input().strip())
B = input().strip()
result = minSteps(n, B)
print(result)

