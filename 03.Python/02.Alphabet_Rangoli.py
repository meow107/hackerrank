#input
#n = 6
# output
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase[:size]
    under = ""
    len_square = 4 * size - 3
    str_keep = ""
    index = size - 1 
    keep_right = ""

    while index >= 0 :
        center =  alphabet[index]
        right = keep_right
        left = right[:: - 1]
        add = "-" 
        right =  center + add + right
        keep_right = right

        line = left + add + right
        if index == 0:
            line = line[1:len(line) - 1]
        line = line.center(len_square,'-')
        print(line)
        if index > 0:
            break_line = "\n"
            if index == 1:
                break_line = ""
            under = break_line + line + under 
        index -= 1

    print (under)

print_rangoli(n)


# REFERENCE -  SO COOL

# n = 6

# import sys,string

# def print_rangoli(size): 
#     w = 2 * size - 1
#     s = string.ascii_lowercase[:size][::-1]
#     print (s)
#     for _ in range(w):
#         i = min(_ , w - _ - 1)
#         print (i)
#         print('-'* (w - 2 * i - 1) + '-'.join(list(s[:i] + s[i]+s[:i][::-1])) + '-' * (w - 2 * i - 1))




# print_rangoli(n)