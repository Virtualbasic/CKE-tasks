numbers = [i[:-1].split() for i in open("dane_ulamki.txt" , "r")]
ulamki = []

def czyskracalny(x):
    print(x)
    licz = x[0]
    mian = x[1]
    def nwd(x1,x2):
        if x2>0:
            return  nwd(x2,x1%x2)
        else:
            return x1

    if nwd(licz,mian) == 1:
        return  True
zasada = []
s =  0
for i in numbers:
    i[0], i[1] = int(i[0]), int(i[1])
    if czyskracalny(i):
        zasada.append(i)


print(len(zasada))
print(s)
