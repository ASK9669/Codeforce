S = input()

count = 0
inside_word = False

for ch in S:
    if ch.isalpha():
        if not inside_word:
            count += 1
            inside_word = True
    else:
        inside_word = False

print(count)
