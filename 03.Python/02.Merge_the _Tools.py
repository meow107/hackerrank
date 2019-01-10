# Input 
# string = "AABCAAADA"
# k = 3

# Output
# AB
# CA
# AD 

def merge_the_tools(string, k):
    n = len(string)
    part = n / k 

    index = 0
    while index < n:
        str_list = list(string[index:index + k])
        unique_list = list(set(str_list))
        unique_list.sort(key = str_list.index)
        print ("".join(unique_list))
        index += k


# merge_the_tools(string, k )