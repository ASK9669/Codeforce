A = input()
B = input()

print(len(A), len(B))
print(A + B)

new_A = B[0] + A[1:]
new_B = A[0] + B[1:]

print(new_A, new_B)
