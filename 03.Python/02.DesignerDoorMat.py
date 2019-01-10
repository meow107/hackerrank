# input
# N = 9
# M = 27

N, M = map(int, input().split())

a = [('.|.'* i).center(M,'-') for i in range(1,N,2)]
for e in a + ['WELCOME'.center(M,'-')] + list(reversed(a)):print(e)



