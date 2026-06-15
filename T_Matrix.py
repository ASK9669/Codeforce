N = int(input())
x = [list(map(int,input().split())) for i in range(N)]
sum1 = 0
for i in range(N):
    for j in range(N):
        if i == j:
            sum1 += x[i][j]
sum2 = 0
for i in range(N):
    for j in range(N):
        if i + j == N-1:
            sum2 += x[i][j]
print(abs(sum1-sum2))
