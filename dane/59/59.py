def rncp(n):
    czynniki = []
    while n%2 == 0:
        czynniki.append(2)
        n //= 2
    for c in range(3, int(n**0.5) +1 , 2):
        while n % c == 0:
            czynniki.append(c)
            n //=c
    if n > 2:
        czynniki.append(n)

    return  czynniki

liczby = [int(i[:-1]) for i in open("liczby.txt" , 'r')]
res = []
palindrony = []
c = 0
for i in range(len(liczby)):
    k = 1
    for j in range(len(rncp(liczby[i]))-1):
        if rncp(liczby[i])[j] != rncp(liczby[i])[j+1]:
            if rncp(liczby[i])[j] % 2 !=0:
                k +=1
            else:
                k =0
                break
    if k == 3 :
        c+=1
        res.append([liczby[i] , rncp(liczby[i]),  k]  )
    if str(liczby[i] + int(str(liczby[i])[::-1])) == str(liczby[i] + int(str(liczby[i])[::-1]))[::-1]:
        palindrony.append([liczby[i] , str(liczby[i] + int(str(liczby[i])[::-1]))])
print(palindrony , end=f" {len(palindrony)}")
#print(c)
#print(res)

