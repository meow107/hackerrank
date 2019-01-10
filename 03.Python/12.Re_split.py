# input
# 100,000,000.000

# output
# 100
# 000
# 000
# 000

# input
# 172
# 16
# 52
# 207
# 172
# 16
# 52
# 117

# output
# .172..16.52.207,172.16.52.117

import re

s = input()
numbers = re.split('[,.]', s)
numbers = filter(None, numbers)
print("\n".join(numbers))