# cook your dish here
def vaccine(D,L,R):
    if D >= 1 and D <=(10**9)  :
        if L >= 1 and L <= (10**9):
            if R >= 1 and R <= (10**9) :
                if D in range(L,R+1):
                    return "Take second dose now"
                elif D>R:
                    return "Too Late"
                else:
                    return "Too Early"
                    
                    
T = int(input(""))
if T >= 1 and T <= (10**5):
    for i in range(T):
        d = input("")
        c = d.split()
        D = int(c[0])
        L = int(c[1])
        R = int(c[2])
        print(vaccine(D,L,R))