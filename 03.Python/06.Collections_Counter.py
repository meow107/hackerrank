# input
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# ouput
# 200


from collections import Counter

X = (int)(input())
all_sizes = list(map(int, input().split()))

counter_sizes = Counter(all_sizes)

N = (int)(input())
i = 0

sum_of_money = 0
while i < N:
    size, price = input().split()
    size, price = int(size) , int(price)

    size_from_shop = counter_sizes[size]
    if size_from_shop > 0:
        
        sum_of_money += price
        counter_sizes[size] = size_from_shop - 1

    i += 1
print(sum_of_money)