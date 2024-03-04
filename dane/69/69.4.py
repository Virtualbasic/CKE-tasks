gens = [i[:-1] for i in open("dane_geny.txt" , "r")]
genotyps = {}
onc = []
silnie_odporne = []
odporne = []
for i in gens:
    if i[::-1] == i:
        silnie_odporne.append(i)
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
                    gt += " "+ tmp
                tmp=""
                f =False
            else:
                tmp+=i[g]
    if gt not in genotyps:
        genotyps[gt] = gt.split()
    onc.append()


for i, v  in genotyps.items():
    accg = ""
    for g in i:
        if not i.isspace():
            accg+=i
    if accg[::-1] == accg:
        odporne+=accg

print(silnie_odporne)
print(len(silnie_odporne))
print(odporne)
print(len(odporne))