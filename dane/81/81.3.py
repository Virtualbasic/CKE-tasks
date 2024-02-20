wierzcholki = [i[:-1].split() for i in open("wspolrzedneTR.txt", "r")]


def obw(z):
    def sq(x):
        return round(x ** 0.5, 2)

    A = [z[0], z[1]]
    B = [z[2], z[3]]
    C = [z[4], z[5]]
    odgAB = sq((((B[0] - A[0]) *(B[0] - A[0])) + ((B[1] - A[1]) *(B[1] - A[1]))))
    odgAC = sq((((C[0] - A[0]) *(C[0] - A[0])) + ((C[1] - A[1]) *(C[1] - A[1]))))
    odgBC = sq((((C[0] - B[0]) *(C[0] - B[0])) + ((C[1] - B[1]) *(C[1] - B[1]))))
    odgab = ((B[0] - A[0]) *(B[0] - A[0])) + ((B[1] - A[1]) *(B[1] - A[1]))
    odgac = ((C[0] - A[0]) *(C[0] - A[0])) + ((C[1] - A[1]) *(C[1] - A[1]))
    odgbc = ((C[0] - B[0]) *(C[0] - B[0])) + ((C[1] - B[1]) *(C[1] - B[1]))
    #cos = ((odgAC**2) - (odgAB **2) - (odgBC**2))/-2*(odgAC*odgAB)

    if odgac +odgab == odgbc or odgbc + odgab == odgac or odgac + odgbc == odgab:
        return [round(odgBC + odgAB + odgAC, 2), z , True]
    return [round(odgBC + odgAB + odgAC, 2), z]
OBWs = []
howmany = 0
for i in range(len(wierzcholki)):
    wierzcholki[i] = [int(j) for j in wierzcholki[i]]
    OBWs.append(obw(wierzcholki[i]))
    try:
        if obw(wierzcholki[i])[2]:
           howmany+=1
    except:
        pass
print(OBWs)
g = []
b = 0
for i in OBWs:
    if i[0] > b:
        b =  i[0]
        g = i
    if i[1][0] == -30:
        print(i)
"3"
print(b)
print(g)
"4"
print(howmany)

