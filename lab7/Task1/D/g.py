n = int(input())
arr = list(map(int,input().split()))

left = 0
right = n-1
while left<right:
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right-=1
print(" ".join(map(str,arr)))
