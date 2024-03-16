def difficult(x):
    if x in range(1,100):
        print("Easy")
    elif x in range(100,200):
        print("Medium")
    elif x in range(200,301):
        print("Hard")
        
    
t = int(input(""))

if t in range(1,51):
    for i in range(t):
        x = int(input(""))
        if x in range(1,301):
            difficult(x)