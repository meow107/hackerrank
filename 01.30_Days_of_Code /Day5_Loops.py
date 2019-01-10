#!/bin/python3

import sys


n = int(input().strip())
i = 0
stop = 10
while i < stop:
    multiple = n * (i + 1)
    print ("%d x %d = %d" % (n, i + 1,multiple ))
    i += 1