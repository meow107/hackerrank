#Cats and a Mouse
# q = int(input().strip())
# for a0 in range(q):
#     x,y,z = input().strip().split(' ')
#     x,y,z = [int(x),int(y),int(z)]
# x : cat A's location
# y : cat B's location
# z : mouse C' location


def print_animal(x,y,z):
    a_to_c = abs (x - z)
    b_to_c = abs (y - z)

    if a_to_c > b_to_c:
        print ("Cat B")
    elif a_to_c < b_to_c :
        print ("Cat A")
    else:
        print ("Mouse C")
        
    

