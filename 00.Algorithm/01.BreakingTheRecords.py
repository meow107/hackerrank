import sys

# Breaking the Records

def getRecord(s):
    # Complete this function
    highest_score = s[0]
    lowest_score = s[0]

    count_hight = 0
    count_low = 0

    for item in s:
        if item > highest_score:
            highest_score = item
            count_hight += 1
        if item < lowest_score:
            lowest_score = item
            count_low += 1
    return (count_hight, count_low)

n = 9
#s = [10,5,20,20,4,5,2,25,1]
s = [3 ,4 ,21, 36 ,10 ,28 ,35 ,5 ,24 ,42]
result = getRecord(s)
print (" ".join(map(str, result)))



