arr_vowels = ['a', 'i', 'e', 'u', 'o']

def is_vowels(ch):
    ch = ch.lower()
    for item in arr_vowels:
        if item == ch:
            return True
    return False

def minion_game(string):
    # Stuart : consonants.
    # Kevin : vowels

    # n - index 
    # consonants index
    # vowels index
    consonants_indexs = []
    vowel_indexs = []

    str_list = list(string)
    n = len(str_list)

    for index,char in enumerate(str_list):
        if is_vowels(char):
            vowel_indexs.append(index)
        else:
            consonants_indexs.append(index)

    sum_consonants = 0
    sum_vowels = 0

    for index in consonants_indexs:
        sum_consonants += (n - index)
    for index in vowel_indexs:
         sum_vowels += (n - index)

    if sum_consonants > sum_vowels:
        print ("Stuart %d" % sum_consonants)
    elif sum_consonants == sum_vowels:
        print("Draw")
    else:
        print("Kevin %d" % sum_vowels)
            

# # Better way
# def minion_game(string):
#     # Stuart : consonants.
#     # Kevin : vowels
#     # consonants = vowels -> "Draw"
#     # Rule : n - index 

#     str_list = list(string)
#     n = len(str_list)
#     sum_consonants = 0
#     sum_vowels = 0
#     for index,char in enumerate(str_list):
#         if is_vowels(char):
#             sum_vowels += n - index
#         else:
#             sum_consonants += n - index

#     if sum_consonants > sum_vowels:
#         print ("Stuart %d" % sum_consonants)
#     elif sum_consonants == sum_vowels:
#         print("Draw")
#     else:
#         print("Kevin %d" % sum_vowels)
            


# input 
# s = "BANANA"
# ouput 
# Stuart 12

# input 
# s = "BANANANAAAS"
# output
# Draw

# minion_game(s)





