# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5 , print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

if __name__ == '__main__':
    n = int(input())
    is_odd = n % 2 != 0
    if is_odd or (n in range(6,21) and is_odd == False):
        print("Weird")
    else:
        print("Not Weird")