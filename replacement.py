N = int(input())
numbers = list(map(int, input().split()))
result = []
for i in numbers:
    if i > 0:
        result.append(1)
    elif i < 0:
        result.append(2)
    else:
        result.append(0)
for i in result:
    print(i, end=' ')
