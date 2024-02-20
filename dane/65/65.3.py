numbers = [i[:-1].split() for i in open("dane_ulamki.txt" , "r")]
ulamki = []

def skrac(x):
    licz = x[0]
    mian = x[1]
    def nwd(x1,x2):
        while x2:
            x1,x2 = x2 , x1%x2
        return x1
    if nwd(licz, mian) == 1 :
        return  x
    else:
        while 
for i in numbers:
    i[0], i[1] = int(i[0]), int(i[1])

print(numbers)