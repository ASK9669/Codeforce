# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         x=len(nums)
# k=0
# for i in range(x):
#             if nums[i]!=val:
#                 nums[k]=nums[i]
#                 k+=1
# return k
# n,m=map(int, input().split())
# count = 0
# for num in range(n , m + 1):
#     is_prime = True
#     for j in range(n, num):
#         if num % j == 0:
#             is_prime = False
#             break
#     if is_prime :
#         count += 1
# if count == 1:
#     print("YES")
# else:
#     print("NO")
##A. Panoramix's Prediction (Codeforces)
# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# a, b = map(int, input().split())
# for i in range(a+1, 51):
#     if is_prime(i):
#         print("YES" if i == b else "NO")
#         break
## Mishka and Game
# n = int(input())
# mishka_wins = 0
# chris_wins = 0
# for _ in range(n):
#     mishka, chris = map(int, input().split())
#     if mishka > chris:
#         mishka_wins += 1
#     elif chris > mishka:
#         chris_wins += 1
# if mishka_wins > chris_wins:
#     print("Mishka")
# elif chris_wins > mishka_wins:
#     print("Chris")
# else:
#     print("Friendship is magic!^^")
## Panoramix's Prediction
##  Prepend and Append
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    count = 0
    if n == 0 :
        print(0)
    elif n == 1:
        print(1)
    else:
        for j in range(int(n/2)):
            if (s[j] == "1") and(s[-(j+1)] == "0"):
                count += 1
            elif (s[j] == "0") and (s[-(j+1)] == "1"):
                count += 1
            else:
                break
        print(n - (2 * count))

        



        
