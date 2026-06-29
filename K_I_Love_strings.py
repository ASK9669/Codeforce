n = int(input())

for i in range(n):
    s, t = input().split()

    m = min(len(s), len(t))

    for i in range(m):
        print(s[i], end="")
        print(t[i], end="")

    print(s[m:] + t[m:])
