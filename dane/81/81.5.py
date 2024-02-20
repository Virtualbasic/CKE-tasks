wierzcholki = [i[:-1].split() for i in open("wspolrzedneTR.txt", "r")]

def xy(z):
    def sq(x):
        return round(x ** 0.5, 2)

    A = [z[0], z[1]]
    B = [z[2], z[3]]
    C = [z[4], z[5]]
    xd = A[0]+C[0] - B[0]
    yd = A[1] + C[1] - B[1]
    if (xd == yd):
        return True


    '''
    odgAB = sq((((B[0] - A[0]) *(B[0] - A[0])) + ((B[1] - A[1]) *(B[1] - A[1]))))
    odgAC = sq((((C[0] - A[0]) *(C[0] - A[0])) + ((C[1] - A[1]) *(C[1] - A[1]))))
    odgBC = sq((((C[0] - B[0]) *(C[0] - B[0])) + ((C[1] - B[1]) *(C[1] - B[1]))))
    srodekPrzekontnejACX = (A[0]+C[0])/2
    srodekPrzekontnejACY = (A[1]+C[1])/2
    srodek = [srodekPrzekontnejACX ,srodekPrzekontnejACY]
    '''
for i in range(len(wierzcholki)):
    wierzcholki[i] = [int(j) for j in wierzcholki[i]]
    if xy(wierzcholki[i]):
        print(wierzcholki[i])

