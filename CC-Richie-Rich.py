# cook your dish here
def rich(a,b,x):
    if a >= 100 and a <= 200 :
        if b >= 100 and b <= 200 :
            if x >= 1 and x <= 50 :
                ans = (b-a)//x
                return ans
                    
                    
T = int(input(""))
if T >= 1 and T <= 21000:
    for i in range(T):
        d = input("")
        c = d.split()
        a = int(c[0])
        b = int(c[1])
        x = int(c[2])
        print(rich(a,b,x))