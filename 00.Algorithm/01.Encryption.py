#!/bin/python3

import sys
import math

# s = 'if man was meant to stay on the ground god would have given us roots'
# s = 'iffactsdontfittotheorychangethefacts'

def encryption(s):
    s = "".join(s.split())
    length_s = len(s)
    sqrt = math.sqrt(length_s)
    left = math.floor(sqrt)
    right = math.ceil(sqrt)
    rows = left
    columns = right

    if right - left >= 2:
        pair1 = left * (left + 1)
        pair2 = (left + 1) * right
        pair3 = left * right
        if pair1 >= length_s:
            rows = left
            columns = left + 1
        elif pair2 >= length_s:
            rows = left + 1
            columns = right      
    s = list(s)
    results = ""
    r = 0
    limit_row = rows - 1 if rows == columns else rows
    while r <= limit_row:
        c = r
        line = ""
        while c < length_s:
            line +=  str(s[c])
            c += columns
        pre = ""
        if r > 0:
            pre = " "
            
        results += ("%s%s" %(pre,line))
        r += 1
    return results


if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)
