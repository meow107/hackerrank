# input
# 5 3
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5

# output
# 90.0 
# 91.0 
# 82.0 
# 90.0 
# 85.5       

N, X = input().split()
N, X = int(N), int(X)

lines = []

for i in range(X):
    line = list(map(float, input().split()))
    lines.append(line)

# The meaning of *  https://stackoverflow.com/questions/29139350/difference-between-ziplist-and-ziplist
# This means you use zip (line1, line2 ,....) -> The * operator unpacks arguments in a function invocation statement.
lines = zip(*lines)
for item in lines:
    print (float(sum(item)) / float(X))

