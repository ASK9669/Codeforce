N = int(input())
result = list(map(int, input().split()))
x = int(input())
for i in range(N):
    if result[i] == x:
        print(i)
        break
if x not in result:
    print(-1)