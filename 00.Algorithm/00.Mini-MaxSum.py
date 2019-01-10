#Mini-Max Sum

a = 1
b = 2
c = 3
d = 4
e = 5

suma = b + c + d + e
sumb = a + c + d + e
sumc = a + b + d + e
sumd = a + b + c + e
sume = a + b + c + d
minsum = min(suma,sumb,sumc,sumd,sume)
maxsum = max(suma,sumb,sumc,sumd,sume)

print ("%d %d" % (minsum,maxsum))
