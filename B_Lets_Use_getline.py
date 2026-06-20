s = input()

for ch in s:
    if ch == '\\':
        break
    print(ch, end='')