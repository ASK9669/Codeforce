n, q = map(int, input().split())
s = list(input())

for i in range(q):
    c = input().split()

    if c[0] == "pop_back":
        s.pop()

    elif c[0] == "front":
        print(s[0])

    elif c[0] == "back":
        print(s[-1])

    elif c[0] == "sort":
        l = min(int(c[1]), int(c[2])) - 1
        r = max(int(c[1]), int(c[2]))
        s[l:r] = sorted(s[l:r])

    elif c[0] == "reverse":
        l = min(int(c[1]), int(c[2])) - 1
        r = max(int(c[1]), int(c[2]))
        s[l:r] = s[l:r][::-1]

    elif c[0] == "print":
        pos = int(c[1]) - 1
        print(s[pos])

    elif c[0] == "substr":
        l = min(int(c[1]), int(c[2])) - 1
        r = max(int(c[1]), int(c[2]))
        print("".join(s[l:r]))

    elif c[0] == "push_back":
        s.append(c[1])
