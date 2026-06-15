t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = []

    for i in range(n):
        mx = arr[i]
        for j in range(i, n):
            mx = max(mx, arr[j])
            ans.append(mx)

    print(*ans)
L_Max_Subarray.py
