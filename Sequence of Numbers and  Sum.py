while True:
    n ,m =map (int,input().split())
    if n>0 and m>0:
    
        if n > m:
            n ,m = m ,n
        sum = 0
        for i in range(n,m+1):
            print(i,end=" ")
            sum += i
        print(f"sum ={sum}")
    else:
        break
