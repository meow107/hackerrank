# 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
# abc
h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
word = "abc"

alphabet = {'a':0, 'b': 1, 'c' : 2, 'd':3, 'e': 4, 'f':5, 'g':6, 'h':7, 'i':8,'j': 9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

max_height = 0

for item in word:
    for k, v in alphabet.iteritems():
        if item == k:
           height = h[v]
           if height > max_height:
               max_height = height
           break
rectangle = max_height *  len(word)
print (rectangle)


            
