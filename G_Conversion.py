s = input()

for ch in s:
    if ch == ',':
        print(' ', end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch.lower(), end='')