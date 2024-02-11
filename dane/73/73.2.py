with open("tekst.txt" , "r") as nm:
    for i in nm:
        ans = {}
        for j in i:
            if not j.isspace() and j !="/n":
                if j in ans:
                    ans[j] +=1
                else:
                    ans[j] = 0
    nm.close()
allletters = 0
for i in ans.values():
    allletters+= i

#procentahe ={}
for k , v  in ans.items():
    print(f" udział {k}:{v} w tekście {round(v/allletters *100, 2)}%")