def chocolates(n, c, m):
    # real number of chocolate without promotion
    n_chocolate_no_promotion = n // c
    sum_of_chocolate = n_chocolate_no_promotion

    # the life is hard when we have promotion
    v = n_chocolate_no_promotion
    while v >= m :
        addmore = v // m
        sum_of_chocolate += addmore
        v = v % m + addmore
    return sum_of_chocolate

t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    print(chocolates(n, c, m))
    




        
    





  
            

        

        
    
