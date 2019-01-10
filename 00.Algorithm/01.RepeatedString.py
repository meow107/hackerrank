# Repeated String
import sys

s = input().strip()
n = int(input().strip())

counter_a_in_one  = 0
counter_a   = 0

dog_tail =  n % len(s)
dog = (int) (n / len(s))

dog_tail_counter = 0

for index,item in enumerate(s):
    if item == 'a':
        counter_a_in_one += 1
        if index < dog_tail:
            dog_tail_counter += 1
counter_a = counter_a_in_one * dog
if dog_tail != 0 :
    counter_a += dog_tail_counter
print (counter_a)

