t = int(input())
for i in range(t):
    n,k = map(int,input().split())

    if k==0:
        print(n)
        
    elif k==n:
        print("0")
    else:
        print(n%k)