N,M = map(int,input().split())
lest= [list(map(int,input().split()))for i in range(N) ]
x = int(input())
found = False
for row in lest:
    if x in row:
        found = True
        break
if found:
    print("will not take number")
else:
    print("will take number")
