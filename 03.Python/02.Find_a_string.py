# input 
# string = "ABCDCDC"
# sub_string = "CDC"
# output
# 2

# input
# string = "ininini"
# sub_string = "ini"
# output
# 3

def count_substring(string, sub_string):
    n = len(string)
    count_substring = 0
    index = -1
    n_substring = len(sub_string)

    while index != -2 :
        try:
            index = string.index(sub_string, index + 1)
        except:
            index = -2
        if index != -2:
            count_substring += 1
    return count_substring
        
# print (count_substring(string,sub_string))