n = int(input())
arr = list(map(int,input().split()))
ma = arr.index(max(arr))
mi = arr.index(min(arr))
arr[mi],arr[ma] = arr[ma],arr[mi]
print(*arr)
