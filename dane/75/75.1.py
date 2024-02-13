class zad:

    def encryption(text, key):

        s = "abcdefghijklmnopqrstuvwxyz"
        A,B = key[0] , key[1]
        szf = ""
        for i in text:
            if (s.index(i) *A )  +B > 25:
                szf += s[((s.index(i) *A )  +B)%26]
            else:
                szf += s[(s.index(i) *A )  +B]
        return szf
key = [5,2]
solution = zad()
text = [i[:-1] for i in open("tekst.txt" , "r")]


z1 = []
for j in text[0].split():
    if len(j) >= 10:
        print(zad.encryption(j,key))

    if j[0] == "d" and j[-1] == "d":
        z1.append(j)

print(z1)

sample = [j.split() for j in [i[:-1] for i in open("probka.txt" , "r")]]


reference =  "abcdefghijklmnopqrstuvwxyz"
szyfr = []
deszyfr = []
ABpermutations = []
for A in range(0, 26):
    for B in range(0 , 26):
        if A!=B:
            ABpermutations.append([A,B])


for i in sample:
    for j in ABpermutations:
        if zad.encryption(i[0],j) == i[1]:
            szyfr.append([i, j ])
        if zad.encryption(i[1],j)  == i[0]:
            deszyfr.append([i,j])
print(deszyfr)

print(zad.encryption(sample[0][1] , [9, 15]))