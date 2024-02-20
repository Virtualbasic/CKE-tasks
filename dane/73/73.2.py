with open("tekst.txt" , "r") as nm:
    for i in nm:
        ans = {}
        for j in i:
            if not j.isspace() and j !="/n":
                if j in ans:
                    ans[j] += 1
                else:
                    ans[j] = 1
    nm.close()

allletters = 0
for i in ans.values():
    allletters+= i

p = []
for k , v  in ans.items():
    p.append([f" udział {k}: {v} w tekście {round(v/allletters *100, 2)}%",round(v/allletters *100, 2) ])
    #print(f" udział {k}: {v} w tekście {round(v/allletters *100, 2)}%")

for i in range(len(p)):
    for j in range(i+1 , len(p)-1):
        if p[j][1] >p[i][1]:
            p[j],p[i] = p[i], p[j]

for g in p:
    print(g[0])