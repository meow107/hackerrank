# 2
# acxz
# bcxz
#Funny String
import sys

def funnyString(s):
    # Complete this function
    #Funny
    #Not Funny
    # reversed string 
    reversed_string = s[::-1]
    i = 1
    is_funny = True
    while i < len(s):
        abs_s = abs(ord(s[i]) - ord(s[i - 1]))
        abs_reversed_string = abs(ord(reversed_string[i]) - ord(reversed_string[i - 1]))
        if abs_reversed_string != abs_s:
            is_funny = False
            break
        i += 1
    if is_funny == True :
        return "Funny"
    else :
        return "Not Funny"

    

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)

