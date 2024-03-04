passwords = [i[:-1] for i in open("hasla.txt" , "r")]
onlynum = []
for pas in passwords:
        f = False
        try:
            if int(pas):
                f = True
        except:
            pass
        finally:
            if f:
                onlynum.append(pas)

usersPasswords = {}

onlyupper = ""
onlylower = ""
onlynumeric = ""

ASCIIcontainer = []
specpasswords = []
for pa in passwords:
    if pa in usersPasswords.keys():
        usersPasswords[pa] +=1
    else:
        usersPasswords[pa] = 1
    f1 = False
    f2 = False
    f3 = False
    for spec in pa:
        if spec.isnumeric():
            onlynumeric+=spec
            onlylower+="_"
            onlyupper+="_"
            f1 =True
        if spec.isupper():
            onlynumeric += "_"
            onlylower += "_"
            onlyupper += spec
            f2 =True
        if spec.islower():
            onlynumeric += "_"
            onlylower += spec
            onlyupper += "_"
            f3=True
    if f1 and f2 and f3:
        specpasswords.append(pa)
    f1 = False
    f2 = False
    f3 = False
    counterv1  = 0
    counterv2  = 0
    counterv3  = 0
    for j  in range(len(onlylower)):
        if counterv3  == 4  or counterv2 == 4  or counterv1  == 4 :
            ASCIIcontainer.append([pa,onlyupper,onlylower,onlynumeric])
        if onlyupper[j] == "_":
            counterv1=0
        if onlynumeric[j] == "_":
            counterv2 = 0
        if onlylower[j] == "_":
            counterv3 = 0
        counterv3 +=1
        counterv2 +=1
        counterv1 +=1
    onlyupper = ""
    onlylower = ""
    onlynumeric = ""


#print(ASCIIcontainer)
#print(len(ASCIIcontainer))
#2
#for k , v in usersPasswords.items():
#    if v >=2:
#        print(f"{k} , {v }")

print(specpasswords)
