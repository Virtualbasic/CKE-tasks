gens = [i[:-1] for i in open("dane_geny.txt" , "r")]
genotyps = {}

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
                    gt += " "+ tmp
                tmp=""
                f =False
            else:
                tmp+=i[g]
    if gt not in genotyps:
        genotyps[gt] = gt.split()


b = 0
handler = []
for i, v  in genotyps.items():
    if len(v) > b:
        b = len(v)
        handler = [i,v]
ndg = 0
handlerv2 = []
for k , v in genotyps.items():
    for i in v:

        if len(i)>ndg:
            ndg = len(i)
            handlerv2= [k,v , len(i)]
print(handler)
print(len(handler[1]))

print(handlerv2)
