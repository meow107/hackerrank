#!/bin/python3

import sys

# Between Two Sets
# Finding numbers range (a[0],b[0]) with i % a[0] && b[0] % i -> save to between_numbers

# check all between_numbers % A
# check all B % between_number 


# n,m = input().strip().split(' ')
# n,m = [int(n),int(m)]
# a = [int(a_temp) for a_temp in input().strip().split(' ')]
# b = [int(b_temp) for b_temp in input().strip().split(' ')]


# a = [2,3,6]
# b = [42,84]


a = [1]
b = [72,48]
# expected : 9


between_numbers = []
i0 = a[0] 
while i0 <= b[0] :
    if (i0 % a[0] == 0) and (b[0] % i0 == 0) :
        between_numbers.append(i0)
    i0 += 1

if len(between_numbers) > 0 :
    # check between numbers % a 
    ia =  0
    removed_item_a = []
    ibtween = 0
    while ibtween < len(between_numbers):
        ia = 0
        isRemoved = False
        while ia < len(a) :
            if between_numbers[ibtween] % a[ia] != 0 :
                isRemoved = True
                break
            ia += 1
        if isRemoved == True :
             removed_item_a.append(between_numbers[ibtween])
             isRemoved = False
            
        ibtween += 1


    if len(removed_item_a) > 0 :
        for item in removed_item_a :
             between_numbers.remove(item)

# check between b % numbers
if len(between_numbers) > 0 :
    ib = 0
    isRemoved = False
    removed_item_b = []
    ibtween = 0
    while ibtween < len(between_numbers):
        ib = 0
        isRemoved = False
        while ib < len(b) :
            if b[ib] % between_numbers[ibtween] != 0 :
                isRemoved = True
                break
            ib += 1
        if isRemoved == True :
             removed_item_b.append(between_numbers[ibtween])
             isRemoved = False
            
        ibtween += 1

    if len(removed_item_b) > 0 :
        for item in removed_item_b :
            between_numbers.remove(item)


print(len(between_numbers))
    
