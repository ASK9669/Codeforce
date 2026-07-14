s = input()

params = s.split('?')[1].split('&')

for p in params:
    key, value = p.split('=')
    print(f"{key}: {value}")
