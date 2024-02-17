publicKey =[3,200] # d , n

def skrot(x):
    S= [ ord(i) for i in "ALGORYTM"]
    while len(x)%8!= 0:
        x+="."
    portions = []
    c = ""
    tmp = []
    for i in x:
        if len(c) != 8:
            tmp.append(i)
        else:
            portions.append(tmp)
            tmp = []
            tmp.append(i)
            c=""
        c+="."
    portions.append(tmp)
    for portion in portions:
        for p in range(len(portion)):
            S[p] = (S[p] +ord(portion[p]))%128
    wynik = ""
    for j in range(len(S)):
        wynik+= chr(65 + (S[j]%26))
    return [wynik , len(x) ,S]
def deszyfr(mark, key):
    d = key[0]
    n = key[1]
    result  = ""
    for  y in mark:
        result+= chr(y*d%n)
    return result

result = []
with open("wiadomosci.txt") as mes:

    for i in mes:
        result.append(skrot(i[:-1]))
mes.close()
print(result)
forwrite = open("Result_data.txt", "w")

forwrite.write(f"{result[0][0]} , {result[0][2]} , {result[0][1]} \n")



marks = [i[:-1].split() for i in open("podpisy.txt", "r")]

deszfrmakrs = []
for i in range(len(marks)):
    for j in range(len(marks[i])):
        marks[i][j] = int(marks[i][j] )

for i in range(len(marks)):
    flag = "Niewiarygodne"
    deszfrmakrs.append(deszyfr(marks[i] , publicKey))
    if deszyfr(marks[i] , publicKey) == result[i][0]:
        flag = "Wiarygodne"
    forwrite.write(f"{i}. {marks[i]}  ,  {deszyfr(marks[i] , publicKey)} , {flag}\n")

print(deszfrmakrs)


forwrite.close()