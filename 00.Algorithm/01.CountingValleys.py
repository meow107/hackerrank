# 8
# UDDDUDUU

# n = 8
# s = "UDDDUDUU"

# n = 8
# s = "DDUUDDUDUUUD"


# n = 8
# s = "UDUDDUUUDUDUDUUDUUDDDDDUDUDDDDUUDDUDDUUUUDUUDUDDDDUDUDUUUDDDUUUDUDDUUDDDUUDDUDDDUDUUDUUDUUDUDDDUUUUU"

# n = int(input().strip())
# s = input().strip()

balance = 0
inFinding = False 
valleys = 0
at_land = 0

for i in range(0, len(s)):
    value = 1
    if s[i] == 'D':
        value = -1
        if at_land == 0:
            inFinding = True

    if inFinding == True :
        balance += value
        if balance == 0 :
            valleys += 1
            inFinding = False

    at_land += value
print (valleys)
        


