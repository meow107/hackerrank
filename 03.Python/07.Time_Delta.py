# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000


# 25200
# 88200

# https://www.tutorialspoint.com/python/time_strptime.htm

import sys
from datetime import datetime

def time_delta(t1, t2):
    # Complete this function
    time_format = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime(t1,time_format)
    t2 = datetime.strptime(t2,time_format)
    return int((abs(t1 - t2)).total_seconds())

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)

