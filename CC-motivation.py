
T = int(input(""))

highest = []

if T >= 1 and T <= 10:
    for i in range(T):
        NX = input()
        NX = NX.split()
        noofmovies = int(NX[0])
        maxspace = int(NX[1])
        for i in range(noofmovies):
            SR = input()
            SR = SR.split()
            space = int(SR[0])
            IMDB = int(SR[1])
            if(space<=maxspace):
                highest.append(IMDB)
        print(max(highest))
        highest = []