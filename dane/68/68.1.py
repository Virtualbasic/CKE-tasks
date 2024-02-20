def check(x):
    if len(x[0]) != len(x[1]):
        return False
    for i in range(len(x[0])):
        if x[0][i] !=  x[0][0]  or x[1][i] !=  x[0][0] :
            return False
    #print(x)
    return  True
teksty =[i[:-1].split() for i in open("dane_napisy.txt" , "r")]

result = open("wynik1.txt", "w" )

def sortstr(x):
    return ''.join(sorted(x))

result2 = open("wynik2.txt" , "w" , encoding="utf8")
count = 0

k = {}
for i in teksty:
    if sortstr(i[0]) not in k:
        k[sortstr(i[0])] = 1
    elif sortstr(i[0]) in k:
        k[sortstr(i[0])] += 1
    if sortstr(i[1]) not in k:
        k[sortstr(i[1])] = 1
    elif sortstr(i[1]) in k:
        k[sortstr(i[1])] += 1
    if sortstr(i[0]) == sortstr(i[1]):
        count+=1
        result2.write(f"{i} , posortowane spełniają warunek anagramu {[sortstr(i[0]) ,sortstr(i[1])]} \n")
    if check(i):
        result.write(f"{i} \n")
result2.close()
result.close()
print(k)

b = 0
s = ""
for l , i in k.items():
    if  i > b:
        s = l
        b = i
print(b ,end=f" {s}")

#print(count)
