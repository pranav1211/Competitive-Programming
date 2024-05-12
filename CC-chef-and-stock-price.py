t = int(input())
for i in range(t):
    s,a,b,c = map(int,input().split())
    
    c = c/100
    news = s * c
    news = s + news
    if news >= a and news <=b:
        print('Yes')
    else:
        print('No')
        