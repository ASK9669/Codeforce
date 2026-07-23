s = input()
n = len(s)

if n == 1:
    print(s)
else:
    total = [0] * 26

    for c in s:
        total[ord(c) - ord('a')] += 1

    left = [0] * 26
    ans = None

    for i in range(n - 1):
        left[ord(s[i]) - ord('a')] += 1

        result = []
        for j in range(26):
            result.append(chr(j + ord('a')) * left[j])
        for j in range(26):
            result.append(chr(j + ord('a')) * (total[j] - left[j]))

        current = "".join(result)

        if ans is None or current < ans:
            ans = current

    print(ans)
