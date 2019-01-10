# Sequence Equation
# n = 3
# sequences = [2,3,1]
# out : 2 3 1

n = int(input().strip())
sequences = [int(temp) for temp in input().strip().split(' ')]

def index_of_value(_list,element):
    for index, item in enumerate(_list):
        if item == element:
            return index 

for index,item in enumerate(sequences):
    #p(p(y)) = x
    #Y = p(y)
    x = index_of_value(sequences,index + 1)
    y = index_of_value(sequences,x + 1) + 1
    print (y)

def index_of_value(_list,element):
    for index, item in enumerate(_list):
        if item == element:
            return index 

for index,item in enumerate(sequences):
    #p(p(y)) = x
    #Y = p(y)
    x = index_of_value(sequences,index + 1)
    y = index_of_value(sequences,x + 1) + 1
    print (y)


    
    
    


    