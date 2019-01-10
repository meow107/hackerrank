# input
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1

# output
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12


N, M = input().split()
N, M = int(N), int(M)
rows = []

for i in range(N):
    columns = list(map(int,input().split()))
    rows.append(columns)
K = int(input())

rows = sorted(rows, key = lambda row :row[K])

for row in rows:
    print(*row, sep = ' ')


    





