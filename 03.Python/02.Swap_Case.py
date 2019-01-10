# -*- coding: utf-8 -*-

# input
# s = "Www.HackerRank.com → wWW.hACKERrANK.COM"
# ouput 
# HackerRank.com presents "Pythonist 2"

# input 
# s = "Pythonist 2 → pYTHONIST 2"
# output
# hACKERrANK.COM PRESENTS "pYTHONIST 2"


def swap_case(s):
    list_s = list(s)
    for index , item in enumerate(list_s):
        str_item = str(item)
        if str_item.islower() :
            list_s[index] = str_item.upper()
        else:
            list_s[index] = str_item.lower()
    return ("").join(list_s)

# Other solution 
# s = "hACKERrANK.COM PRESENTS pYTHONIST 2"
# s = s.swapcase()
# print (s)
