n = int(input())
cnt =0
for _ in range (0,n):
    digit = int(input())
    if digit==0:
        cnt+=1
print(cnt)