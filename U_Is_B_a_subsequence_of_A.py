A, B = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

j = 0

for i in range(A):
    if j < B and x[i] == y[j]:
        j += 1

if j == B:
    print("YES")
else:
    print("NO")

# U_Is_B_a_subsequence_of_A.py
