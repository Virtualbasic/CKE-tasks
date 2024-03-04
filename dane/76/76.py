s = [i[:-1] for i in open("szyfr1.txt", "r")]
S = s[:-1]
slowa= []
slowo =[]
for i in S:
    for j in i:
        slowo.append(j)
    slowa.append(slowo)
    slowo = []
P = []
tmp =""
for i in s[6]:
    if  i.isspace():
        P.append(int(tmp)-1)
        tmp = ""
    else:
        tmp += i
P.append(int(tmp)-1)

for s in slowa:

    for przesuniencie in range(len(s)):
        s[przesuniencie] ,s[P[przesuniencie]] =  s[P[przesuniencie]],s[przesuniencie]

t =""
for szyfr in slowa:
    for i in szyfr:
        t+=i
    print(t)
    t=""