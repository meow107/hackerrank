import re

def is_phone_number(s):
    #patern = '(7|8|9)(\d{9})$'
    patern = '^([7-9]\d{9})$'
    m = re.search(r'%s' % patern, s)
    return(bool(m))
    
n = int(input())
for i in range(n):
    is_phone = is_phone_number(input())
    print("YES" if is_phone else "NO")








