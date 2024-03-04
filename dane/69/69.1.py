gens = [i[:-1] for i in open("dane_geny.txt" , "r")]
genotyps = {}
for i in gens:
    if len(i) not in genotyps.keys():
        genotyps[len(i)] = 1
    else:
        genotyps[len(i)] += 1
print(len(genotyps))
b = 0
for v in genotyps.values():
    if v > b:
        b = v

print(b)