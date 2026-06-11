N = int(input())
for i in range(N):
    s = N-i -1
    x = 2*i+1
    print(" "*s+ "*"* x)
for i in range(N-1,-1,-1):
    s = N-i -1
    x = 2*i+1
    print(" "*s+ "*"* x)
