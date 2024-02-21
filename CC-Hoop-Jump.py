def jump(n):
    if(n%2==0):
        pass
    else:
        j = n    
        i = j//2
        print(i+1)
        


T = int(input(""))
for i in range(T):
    N = int(input(""))
    jump(N)
    i+=1
