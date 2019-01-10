# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

import sys

if __name__ == '__main__':
    
    out_list = []  
    N = int(raw_input())
    i = 0
    while i < N:
        independents = (str)(raw_input()).split(' ')
        command = independents[0]
        if command == "insert":
            index = (int)(independents[1])
            item = (int)(independents[2])
            out_list.insert(index,item)
        elif command == "print":
            print(out_list)
        elif command == "remove":
            item = (int)(independents[1])
            out_list.remove(item)
        elif command == "append":
            item = (int)(independents[1])
            out_list.append(item)
        elif command == "sort":
            out_list.sort()
        elif command == "pop":
            out_list.pop()
        elif command == "reverse" :
            out_list.reverse()           
        i += 1




