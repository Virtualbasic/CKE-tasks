T = [i[:-1].split() for i in open("trojki.txt" , "r")]
#for j in range(len(T)):T[j] = list(map(lambda x:int(x), T[j]))

for i in T:
    num = ''.join([i[0], i[1]])
    tmp = 0
    for g in num:
        tmp+=int(g)
    if tmp == int(i[2]):
        print(i)



#print(T)