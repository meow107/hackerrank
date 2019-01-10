#Taum and B'day
import sys

def count(b,w,x,y,z):
    change_x = z + y
    change_y = z + x

    if x == y or (x <= change_x and y <= change_y) :
        return b * x + w * y
    if x > change_x and y < change_y:
        return b * change_x + w * y
    if x < change_x and y > change_y:
        return b * x + w * change_y
    if x > z and y > z:
        return b * change_x + w * change_y
        


t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    print (count(b,w,x,y,z))
  
