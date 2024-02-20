def check(points):
    for i in points:
        if i <= 0:
            return False
    return  True

Points = []
def checkIfOnsame(points):
    P = []
    c = 0
    tmp = []
    for i in points:
        if c == 2:
            P.append(tmp)
            tmp = []
            c = 0
        tmp.append(i)
        c+=1
    P.append(tmp)
    A = P[0]
    B = P[1]
    C = P[2]

    if (B[1]-A[1])*(C[0]-B[0]) == (C[1]-B[1])*(B[0]-A[0]):
        print([P , "na tej samej prostej "])
        Points.append(P)


points = [i[:-1].split() for i in open("wspolrzedne.txt", "r")]
zalerzosc1 = []
for i in range(len(points)):
    points[i] = [int(j) for j in points[i]]
    if check(points[i]):
        zalerzosc1.append(points[i])
    if checkIfOnsame(points[i]):
        print(checkIfOnsame(points[i]))
print(zalerzosc1)
print(len(Points))




