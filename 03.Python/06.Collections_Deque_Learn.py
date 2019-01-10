
from collections import deque

d = deque()
print("Append : 1")
d.append(1)
print(d)

print("Append left : 2")
d.appendleft(2)
print(d)

print("Clear")
d.clear()
print(d)

print("Extend '1'")
d.extend('1')
print(d)

print("Extend left '234'")
d.extendleft('234')
print(d)

print("count '1'")
print(d.count('1'))

print("pop")
d.pop()
print(d)

print("pop left")
d.popleft()
print(d)

print("extend '7896'")
d.extend('7896')
print(d)

print("remove '2'")
d.remove('2')
print(d)

print("reverse")
d.reverse()
print(d)

print("rotate 3")
d.rotate(3)
print(d)

