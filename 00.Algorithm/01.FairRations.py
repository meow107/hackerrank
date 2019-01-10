import sys

def check_even(array):
    for item in array:
        if item % 2 != 0:
            return False
    return True

def fairRations(B):
    
    # count number of odd 
    count_odd = 0
    for item in B:
        if item % 2 != 0:
            count_even += 1
    if count_even % 2 != 0 :
        return "NO"

    # if number of odd is even
    count = 0
    for index in range(N):
        if B[index]  % 2 != 0:
            B[index] += 1
            B[index + 1] += 1        
            count += 2

    return str(count)
        

if __name__ == "__main__":
    N = int(input().strip())
    B = list(map(int, input().strip().split(' ')))
    result = fairRations(B)
    print(result)