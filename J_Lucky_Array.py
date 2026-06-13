n = int(input())
result = list(map(int,input().split()))
x = result.count(min(result))
if x % 2 != 0:
    print("Lucky")
else:
     print("unlucky")