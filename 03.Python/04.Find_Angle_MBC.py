# input
# 10
# 10

# outpur
# 45°

# -*- coding: utf-8 -*-

import math

local_encoding = 'cp850' 
AB = (int)(input())
BC = (int)(input())
AC = math.sqrt(AB ** 2 + BC ** 2)
cosine_theta = (float)(BC) / (float)(AC)
degree_theta = round(math.degrees(math.acos(cosine_theta)))
print("%d°" % (degree_theta))


