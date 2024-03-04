T = [i[:-1].split() for i in open("trojki.txt" , "r")]
for j in range(len(T)):T[j] = list(map(lambda x:int(x), T[j]))
handler = []
ciong = 0
cc = 0
for t in T:
    b= 0
    s = 0
    for i in t:
        s+=i
        if i >b:
            b = i
    if b < s -b:
        cc+=1
        handler.append(t)
    else:
        if cc > ciong:
            ciong = cc
            cc = 0
        cc=0
print(len(handler))
print(ciong)