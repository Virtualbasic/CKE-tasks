gens = [i[:-1] for i in open("dane_geny.txt" , "r")]
genotyps = {}
mutation = "BCDDC"
mutations = 0
for i in gens:
    tmp =""
    gt = ""
    f=False
    for g in range(len(i)-2):
        if not f:
            if i[g] + i[g + 1] == "AA" and i[g + 2] != "A":
                f = True
        if f:
            if len(tmp)>2and  tmp[-1] + tmp[-2] == "BB":
                if tmp not in genotyps:
                    gt +=tmp
                tmp=""
                f =False
            else:
                tmp+=i[g]
    if gt not in genotyps:
        genotyps[gt] = 1
    if mutation in gt:
        mutations+=1


s =0
for i, v  in genotyps.items():
    #print(f"{i} , {v}")
    s+=1
print(genotyps)
print(s)
print(mutations)