n = int(input())
arr = list(map(int,input().split()))
uniq=list(set(arr))
uniq.sort(reverse=True)
print(uniq[1])