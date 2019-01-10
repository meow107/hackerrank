# input
# 5

# output
# [0, 1, 1, 8, 27]

n = int(input())


cube = lambda x : x ** 3

def fibonacci(n):
    fibonaci = lambda i : i if i < 2 else fibonaci(i - 1) + fibonaci(i - 2)
    fibonaci_sequence = map(fibonaci, range(n))
    return fibonaci_sequence

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


