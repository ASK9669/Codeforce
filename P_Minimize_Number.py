n = int(input())
arr = list(map(int, input().split()))

ans = float('inf')

for x in arr:
    cnt = 0
    while x % 2 == 0:
        cnt += 1
        x //= 2
    ans = min(ans, cnt)

print(ans)