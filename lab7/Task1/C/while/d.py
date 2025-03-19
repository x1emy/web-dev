n = int(input())
power = 1
while power<=n:
    print(power,end=" ")
    power *=2

if power == n:
    print("YES")
else:
    print("NO")