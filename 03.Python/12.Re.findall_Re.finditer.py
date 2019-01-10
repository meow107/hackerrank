import re

# print(re.findall(r'\w','http://www.hackerrank.com/'))

# print(re.finditer(r'\w','http://www.hackerrank.com/'))
# print (*map(lambda x : x.group(),re.finditer(r'\w', 'http://www.hackerrank.com/')))

# input
# rabcdeefgyYhFjkIoomnpOeorteeeeet

# output
# ee
# Ioo
# Oeo
# eeeee

# input
# abaabaabaabaae

# output
# aa
# aa
# aa


s = input()
result = re.findall(r'[aeiouAEIOU]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]',s)

if result :
    for item in result:
        print(item[0:len(item) - 1])
else:
    print(-1)

