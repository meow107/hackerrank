import re

def is_valid_mail(inmail):
    patern = '<([A-Za-z0-9][A-Za-z0-9-._]+)@([A-Za-z]+)\.([A-Za-z]{1,3})>'
    match = re.search(r'%s' % patern, inmail)
    return bool(match)

n = int(input())
for i in range(n):
    input_s =  input()
    if is_valid_mail(input_s):
        print(input_s)

