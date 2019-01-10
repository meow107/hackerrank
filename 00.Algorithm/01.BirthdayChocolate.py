import sys
# Birthday Chocolate
def getWays(squares, d, m):
    # Complete this function
    count = 0
    len_square = len(squares) 
    if len_square == 1 and squares[0] == d:
        count = 1
    elif len_square > 0:
        for i in range(0, len_square):
            #print (("i = %d, len = %d") %(i,len_square))
            sum = 0
            end = i + m
            # Missing testcase here : missing some ending elements
            if end <= len_square :
                #print (("i + m = %d") %(i + m))
                for j in range(i, end):
                    sum += squares[j]
                if sum == d :
                    count += 1
    return count
            
n = 5
s = [1,2,1,3,2]
d = 3
m = 2

# s = [4]
# d = 4
# m = 1

result = getWays(s, d, m)
print(result)