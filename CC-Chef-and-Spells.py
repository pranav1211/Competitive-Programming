def maxhp(a,b,c):
    lst = [a,b,c]
    lst.sort()
    print(lst[-2]+lst[-1])

t = int(input())
if t >=1 and t <= (10**4):
    for i in range(t):
        a,b,c = map(int,input().split())
        maxhp(a,b,c) 