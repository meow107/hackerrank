# input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5

# out 
# 4

n = int(input())
s = set(map(int, input().split())) 
numer_commands = int(input())

i = 0 
while i < numer_commands:
    tmp = input()
    if tmp == "pop":
        s.pop()
    else:
        comand , with_numer = tmp.split() 
        if comand == "remove":
            with_numer = (int)(with_numer)
            s.remove(with_numer)
        elif comand == "discard":     
            with_numer = (int)(with_numer)
            s.discard(with_numer)
    i += 1

print(sum(s))

