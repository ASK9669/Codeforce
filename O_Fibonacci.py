n = int(input())
a, b = 0, 1
arr = []
for i in range(n-1):
    a, b = b, a + b
    arr.append(a)
print(a)
