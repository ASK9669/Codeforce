# A , B = map(int,input().split())
# s = input()
# for i in range(len(s)):
#     if s[A]== "-":
#         print("Yes")
#         break
# else:
#     print("No")
A, B = map(int, input().split())
s = input()

if len(s) == A + B + 1 and s[A] == "-":
    if s[:A].isdigit() and s[A+1:].isdigit():
        print("Yes")
    else:
        print("No")
else:
    print("No")