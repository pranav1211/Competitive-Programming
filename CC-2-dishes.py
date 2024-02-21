def jump(max,sum):
    count = 0;
    for i in range(max+1):
        j = sum-i
        if j>=0 and j<=max:
            count+=1
    print(count-1)
    
        


T = int(input(""))
for i in range(T):
    NS = input("")
    ns = NS.split()
    max = int(ns[0])
    sum = int(ns[1])
    jump(max,sum)