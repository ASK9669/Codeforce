Q = int(input())

Key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
Original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

S = input()

ans = []

if Q == 1:
    for ch in S:
        idx = Original.index(ch)
        ans.append(Key[idx])
else:
    for ch in S:
        idx = Key.index(ch)
        ans.append(Original[idx])

print("".join(ans))
