s = input()
x = len(s) - 1

for i in s:
    if i != s[x]:
        print("NO")
        break
    x -= 1
else:
    print("YES")
