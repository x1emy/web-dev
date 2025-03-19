import math
n = int(input())
i = 0
while i<n:
    i+=1
    if math.isqrt(i)**2==i:
        print(i)