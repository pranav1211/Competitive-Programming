def checker(a,b,case1,case2):    
    if a in case1 and b in case1:
      print(1)
    elif a in case2 and b in case2:
      print(2)
    else:
      print(0)  
    
t = int(input(""))

if t in range(1,289):
    for i in range(t):
        cases = input("")
        a,b,a1,b1,a2,b2 = map(int,cases.split())
               
        case1 = []
        case1.extend([a1,b1])
        case2 = []
        case2.extend([a2,b2])
        
        if a!=b and a1!=b1 and a2!=b2 and a1!=a2 and b1!=b2:
            checker(a,b,case1,case2)