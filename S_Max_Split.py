s = input()

ans = []
cntL = 0
cntR = 0
start = 0

for i in range(len(s)):
    if s[i] == 'L':
        cntL += 1
    else:
        cntR += 1

    if cntL == cntR:
        ans.append(s[start:i+1])
        start = i + 1

print(len(ans))
for x in ans:
    print(x)
S_Max_Split.py
