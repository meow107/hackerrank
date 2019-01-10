# 4  
# 4.0O0
# -1.00
# +4.54
# SomeRandomStuff

# False
# True
# True
# False

import re

def validate(s):
    
    all_rule = False
    rule_4  = True
    try :
        float(s)
    except:
        rule_4 = False
    
    if rule_4:
        rule_3 = True
        i = - 1
        count_dot = 0
        while i < len(s):
            index_dot = re.search(r".", s[i +  1:])
            if index_dot != None:
                count_dot += 1
                if count_dot == 2:
                    rule_3 == False
                    break
                i = index_dot.end()
            else :
                rule_2 = False
                break

        if rule_3:
            rule_2 = True
            index_dot = re.search(r".", s).end()
            if len(s[index_dot:]) <= 1:
                rule_2 = False
            
            if rule_2:
                all_rule = True
    return all_rule
                
n = int(input())
for i in range(n):
    user_input = input()
    print (validate(user_input))
   


