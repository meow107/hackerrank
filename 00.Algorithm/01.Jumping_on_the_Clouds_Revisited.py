#Jumping_on_the_Clouds_Revisited


# 8 2 (k)
# 0 0 1 0 0 1 1 0
# Sample Output

# #92
# step = (i + k) % n
# step = 0 stop
# e = - 1 to run , if step = thunder , e -2

# k = 2
# n = 8
# c = [0,0,1,0, 0, 1 ,1, 0]

k = 1
n = 16
c = [1 ,1, 1, 1 ,1 ,1 ,1, 1 ,1 ,1 ,1 ,1 ,1 ,1, 1 ,1]

i = 0
i = (i + k ) % n
E = 100
while i != 0 :
    E -= 1
    if c[i] == 1:
        E-= 2
    i = (i + k) % n
if E > 0 :
    if c[0] == 1:
        E -= 2
    print (E - 1)
else:
    print(0)