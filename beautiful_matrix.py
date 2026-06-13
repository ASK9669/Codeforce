import sys

for i in range(5):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        if v == 1:
            print(abs(i - 2) + abs(j - 2))
            sys.exit()
