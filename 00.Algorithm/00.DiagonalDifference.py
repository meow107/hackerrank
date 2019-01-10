import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

print (a)

left = a[0][0]
right = a[n - 1][0]

leftRow = 0
leftColumn = 0


rightRow = 0
rightColumn = n - 1

sumLeft = 0
sumRight = 0

row = 0
colunm = 0
#print ("n %d" %(n))

while row < n : 
    colunm = 0
    while  colunm < n:
        # left
        if leftRow < n and leftColumn < n:
            if (a[row][colunm] == a[leftRow][leftColumn]):
                sumLeft += a[row][colunm]
                leftRow += 1
                leftColumn += 1
                print ("left---(%d,%d)"%(row,colunm))
        # right 

        if rightColumn >= 0 and rightRow < n:
            if (a[row][colunm] ==  a[rightRow][rightColumn]):
                sumRight += a[row][colunm]
                rightRow += 1
                rightColumn -= 1
                print ("right---(%d,%d)"%(row,colunm))
        # print ("(%d, %d)" % (row, colunm))
        # print ("a---%d"% a[row][colunm])
        colunm += 1
    row += 1
  
print("left %d -- right %d--- result ----%d" % (sumLeft,sumRight ,abs(sumLeft - sumRight)))



