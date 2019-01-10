#Modified Kaprekar Numbers
#https://en.wikipedia.org/wiki/Kaprekar_number

import sys

p = input().strip()
q = input().strip()

p = int(p)
q = int(q)

q += 1

def sum_splipt_two(n):
    
    if n < 10:
        return n

    str_num = str(n)
    len_n = len(str_num)
    mid_index = (int)(len_n / 2)
        
    first = str_num[:mid_index]
    after = str_num[mid_index:]

    first_num = int(first)
    after_num = int(after)

    if after_num == 0 :
        return -1

    return first_num + after_num

is_kaprekar = False
str_kaprehar = ""
for i in range(p,q):
    square_i = i ** 2
    sum_square = sum_splipt_two(square_i)
    if i == sum_square:
        if i == q -1 :
            str_kaprehar += str(i)
        else:
            str_kaprehar += (str(i) + " ")
        
if str_kaprehar == "":
    print("INVALID RANGE")
else:
    print(str_kaprehar)


def sum_splipt_two(n):
    
    if n < 10:
        return n

    str_num = str(n)
    len_n = len(str_num)
    mid_index = (int)(len_n / 2) 
    first = str_num[:mid_index]
    after = str_num[mid_index:]

    first_num = int(first)
    after_num = int(after)

    if after_num == 0 :
        return -1

    return first_num + after_num

is_kaprekar = False
str_kaprehar = ""
for i in range(p,q):
    square_i = i ** 2
    sum_square = sum_splipt_two(square_i)
    if i == sum_square:
        if i == q -1 :
            str_kaprehar += str(i)
        else:
            str_kaprehar += (str(i) + " ")
        
if str_kaprehar == "":
    print("INVALID RANGE")
else:
    print(str_kaprehar)
