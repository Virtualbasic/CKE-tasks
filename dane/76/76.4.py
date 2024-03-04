s = [i for i in open("szyfr3.txt", "r")]
S = [g for g in s[0]]
P = [6, 2, 4, 1, 5, 3]
for i in range(len(P)):P[i]-=1
n = len(S)
j = n-1
while j>=0:

    S[j], S[P[j%6]] = S[P[j%6]] , S[j]
    print(S)
    j-=1



print(''.join(S))