n = int(input())
A = list(map(int, input().split()))

for i, x in enumerate(A):
    if x <= 10:
        print(f"A[{i}] = {x}")
