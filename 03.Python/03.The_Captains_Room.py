# input
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

# output
# 8

k = (int)(input())
room_list = list(map(int, input().split()))
room_list.sort()

step = 0
n = len(room_list)

while step < n:
    begin = step
    end = step + k - 1
    if end > n -1:
        end = n - 1
    if room_list[begin] != room_list [end] or begin == end :
        print (room_list[step])
        break
    step = end + 1


# # The best solution
# myset = set(arr)
# # if catains have full k people
# sum_full = sum(myset) * k
# sum_real = sum (arr)

# # We have only catains, so the distance from full and real is (k - 1) * captains_number
# # So get the number , we divide the remain to (k - 1)
# captain_number = (sum_full - sum_real) // (k - 1)
# print (captain_number)








