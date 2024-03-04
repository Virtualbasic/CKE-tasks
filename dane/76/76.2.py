s = [i[:-1] for i in open("szyfr2.txt", "r")]
S = [g for g in s[0]]
P = []
tmp =""
for i in s[1]:
    if  i.isspace():
        P.append(int(tmp)-1)
        tmp = ""
    else:
        tmp += i
P.append(int(tmp)-1)

#c = 0
#while len(P) < len(S):
#    if c >14:
#        c = 0
#    P.append(P[c])
#    c+=1

print(P)
n = len(P)
for i in range(len(S)):
    S[i] , S[P[i%n]] = S[P[i%n]] , S[i]


t =""
for d in S:
    t+=d
print(t)