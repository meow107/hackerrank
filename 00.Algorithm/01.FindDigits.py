import sys

def count_diviable_digit(N):
    init_N = N
    count_diviable_N = 0
    remaining = 0 
    while init_N > 0:
        remaining = init_N % 10
        if remaining != 0 and N % remaining == 0:
            count_diviable_N += 1

        init_N = (int)(init_N / 10)
  
    return count_diviable_N


# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     print (count_diviable_digit(n))
    
t = [12, 1012]

for n in t:
     print (count_diviable_digit(n))


