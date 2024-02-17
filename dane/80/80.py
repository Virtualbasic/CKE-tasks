t = [int(i[:-1]) for i  in open("dane_trojkaty.txt", "r") ]

permt = []

def perms(n):
    r = []
    for i in range(n):
        for j in range(n):
            for g in range(n):
                if g!= i and g!=j and i!=j:
                    r.append([i,j,g])
    return r
hits = []
for nums in range(len(t)-2):
    temp = [t[nums],t[nums+1], t[nums+2]]
    r = perms(3)
    for i in r:
        if temp[i[0]]**2 == temp[i[1]]**2 + temp[i[2]]**2:
            hits.append([t[nums],t[nums+1], t[nums+2]])
            break

biggest = []
ref = 0
c= 0
i = 0
while i <len(t):
    if c ==3:
        break
    if c ==1 or c==2:
        i =0
    for j in  t:
        if j > ref and j not in biggest:
            ref = j
    if ref not in biggest:
        biggest.append(ref)
    ref = 0
    c +=1
    i+=1

print(biggest)
print(biggest[0] + biggest[1] + biggest[2])