N = int(input())
numbers = list(map(int, input().split()))

a = 0
b = N - 1

while a < b:
    if numbers[a] != numbers[b]:
        print("NO")
        break
    a += 1
    b -= 1
else:
    print("YES")
