# 2
# hereiamstackerrank
# hackerworld

# test_case = ["knarrekcah","hackerrank","hackeronek","abcdefghijklmnopqrstuvwxyz","rhackerank","ahankercka","hacakaeararanaka","hhhhaaaaackkkkerrrrrrrrank","crackerhackerknar","hhhackkerbanker"]

# NO
# YES
# NO
# NO
# NO
# NO
# YES
# YES
# NO
# NO

import sys

def contain_hackerrank(s):
    hackerrank = "hackerrank"
    n_hackerran = len(hackerrank)
    n_s = len(s)
    i = 0
    j = 0
    current_find = -2
    while i < n_hackerran:
        #print ("letter = %c i = %d=============================" % (s[i],i))
        if current_find >= 0:
            j = current_find + 1
            current_find = -1
        else :
            if i > 0:
                break
        while j < n_s:
            #print ("j = %d " % j)
            if hackerrank[i] == s[j]:
                current_find = j
                #print("letter = %c finding index = %d" %(s[j], j))
                break
            else:
                current_find = -1
            j += 1
        i += 1
    if current_find >= 0:
        return "YES"

    return "NO"


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    print (contain_hackerrank(s))
    # your code goes here



