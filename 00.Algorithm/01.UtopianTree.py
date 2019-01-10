#Utopian Tree
import sys

def count_full_cycle(loops):
    height =  1
    for i in range(0, loops):
        height = (height * 2) + 1 
    return height
        
def count_height(cycles):
    # spring * 2
    # sumer +  1
    height = 1
    if cycles == 0:
        pass
    elif cycles == 1:
        height *= 2
    elif cycles == 2:
        height = count_full_cycle(1)
    else:
        loops = (int)(cycles / 2)
        if cycles % 2 == 0 :
            height = count_full_cycle(loops)
        else:
            height = count_full_cycle(loops) * 2
    return height
            



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print (count_height(n))
            
        
        
      
    




