n = 5
k = 4
height = [1,6,3,5,2]

height.sort(reverse = True)
number_beverage = 0

if k >= height[0]:
    number_beverage = 0
else:
    number_beverage = abs(height[0] - k)

print (number_beverage)




