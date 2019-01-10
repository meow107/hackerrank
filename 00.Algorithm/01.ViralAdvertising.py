#Viral Advertising


#n = 3
n = int(input().strip())
m = 5
i = 0

likes = 0

while i < n:
    like  = (int) (m / 2)
    dislike = m - like
    shared = like * 3

    likes += like
    m = shared
    i += 1

print (likes)
