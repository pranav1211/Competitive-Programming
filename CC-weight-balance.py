t = int(input())
for i in range(t):
    w1,w2,x1,x2,m = map(int,input().split())

    change = w2-w1
    minwt = x1 * m
    maxwt = x2 * m
    
    if change >= minwt and change <= maxwt:
        print(1)
    else:
        print(0)
        