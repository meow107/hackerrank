# input 
# n = 10
# array = [161, 182 ,161 ,154 ,176, 170 ,167 ,171 ,170, 174]

# output
# 169.375

def average(array):
   array = set(array)
   return sum(array) / len(array)

