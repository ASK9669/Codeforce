N,M = map(int,input().split())
arr = [list(map(int,input().split()))for i in range(N)]
for i in range(len(arr)):
	print(*arr[i][::-1])
