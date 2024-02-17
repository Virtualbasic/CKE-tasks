with open("dokad.txt", "r") as text:
    alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "LUBIMYCZYTAC"
    szyfr = ""
    indexforkey = 0
    howmanyrepeat = 0
    for i in text:
        for j in i:
            flag = False
            if j.isspace() or j =="," or j ==".":
                flag = True
                szyfr+=j
            else:
                if indexforkey> 11:
                    indexforkey= 0
                    howmanyrepeat+=1
                limiter = alfa.index(j)
                przes  = (limiter -  alfa.index(key[indexforkey]) -1)
                if przes < 0:
                    przes*=-1
                print(przes)
                if limiter + przes > 25:
                    tmp = 25 - limiter
                    szyfr+= alfa[przes-tmp]
                else:
                    szyfr+= alfa[przes]
            if flag:
                pass
            else:
                indexforkey+=1
    print(szyfr)
    print(howmanyrepeat+1)