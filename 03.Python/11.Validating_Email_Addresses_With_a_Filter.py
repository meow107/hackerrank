
# input 
# 3
# lara@hackerrank.com
# brian-23@hackerrank.com
# britts_54@hackerrank.com

# output
# ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

# input
# 5
# itsme@gmail
# @something
# @something.com
# @something.co1
# sone.com

# output
# []

def fun(s):
    s = str(s)
    if s[0] == '@' or s[len(s) - 1] == '.':
        return False
    at_index = s.find('@')
    dot_index = s[::-1].find('.') 
    user_name = s[:at_index]
    if dot_index == -1 or user_name == -1:
        return False
    dot_index = len(s) - 1 - dot_index
    website_name = s[at_index + 1: dot_index]
    extension = s[dot_index + 1:]
    user_name_filter = list(filter(lambda x: (str(x).isalpha() or str(x).isdigit() or str(x) == '-' or str(x) == '_' ), user_name))
    if len(user_name) == len(user_name_filter):
        website_name_filter = list(filter (lambda x : ( str(x).isalpha() or str(x).isdigit()), website_name))
        if len(website_name) == len(website_name_filter):
            if len(extension) <= 3:
                return True
    return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)