#ACM ICPC Team
import sys

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
   topic_t = str(input().strip())
   topic.append(topic_t)

i = 0
max_value = 0
xor_str_array = []
while i < len(topic):
    j = i + 1
    max_xor = 0
    while j < len(topic) :
        xor_int = int(topic[i],2)  | int(topic[j],2)
        xor_str = bin(xor_int)[2:].zfill(len(topic[i]))
        xor_str_array.append(xor_str)

        # print ("i =" + topic[i] + " j = " + topic[j] + " rs = " + xor_str )
        count_1 = xor_str.count("1")
        # print (count_1)
        max_xor = max(count_1, max_xor)
        j += 1
    max_value = max(max_xor,max_value)
    i += 1


count_index = 0
for item in xor_str_array:
    if item.count("1") == max_value:
        count_index += 1
print (max_value)
print (count_index)
    
    



