# alice = [5 ,25 ,50 ,120]
# scores = [100, 100, 50 ,40 ,40 ,20, 10]
# out 6 4 2 1

import sys

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

# your code goes here
scores = list(set(scores))
scores.sort()
keep_index = 0
n_score = len(scores)
for item in alice:
    if item < scores[0]:
        print (n_score + 1)
    elif item == scores[0]:
        print(n_score)
    elif item >= scores[n_score - 1]:
        print (1)
    else:
        for index in range(keep_index, n_score):
            if item < scores[index]:
                print (n_score - index + 1)
                keep_index = index
                break


    

                
        
    
            
                

    