# Input
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France 

# Output
# 5

n = (int)(input())
set_countries = set()
i = 0
while i < n:
    temp = input()
    set_countries.add(temp)
    i += 1
print (len(set_countries))