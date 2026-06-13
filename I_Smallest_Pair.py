T = int(input())

for i in range(T):
    n = int(input())
    y = list(map(int, input().split()))

    arr = []

    for i in range(n):
        for j in range(i + 1, n):
            arr.append(y[i] + y[j] + j - i)

    print(min(arr))