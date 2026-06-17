n, m = map(int, input().split())

grid = [input() for _ in range(n)]

r, c = map(int, input().split())

r -= 1
c -= 1

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

for dr, dc in directions:
    nr = r + dr
    nc = c + dc

    if grid[nr][nc] != 'x':
        print("no")
        break
else:
    print("yes")
