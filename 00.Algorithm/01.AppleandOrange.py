#Apple and Orange
s = 7
t = 11
a = 5
b = 15
m = 3
n = 2
apple = [-2,2,1]
orange = [5, -6]
apple_count = 0
orange_count = 0
if s >= a and t <= b:
    # for apple
    for item in apple:
        d = item + a
        # just right > 0
        if d >= 0 and d >= s and d <= t:
            apple_count += 1
    # for orange
    for item in orange:
        d =  d = item + b
        if d >= s and d <= t:
            orange_count += 1
        
    
print (apple_count)
print (orange_count)
