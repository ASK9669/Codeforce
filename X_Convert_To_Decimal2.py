t = int(input())

for _ in range(t):
    n = int(input())

    ones = 0

    while n:
        ones += n % 2
        n //= 2

    print((1 << ones) - 1)