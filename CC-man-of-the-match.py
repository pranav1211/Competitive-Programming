T = int(input(""))

mom = []

for i in range(T):
    for j in range(22):
        AB = input()
        AB = AB.split()
        A = int(AB[0])
        B = int(AB[1])
        score = A + (B*20)
        mom.append(score)
    highest = max(mom)
    print(mom.index(highest)+1)
    mom = []