with open("liczby2.txt" , "r")  as num:
    accC = [0]
    for c in num:
        accnum = c.replace("\n" , "")
        ndm = 0
        if int(accnum) > accC[-1]:
            accC.append(int(accnum))
            ndm = len(accC)
        else:
            accC = [0]
num.close()
print(accC , ndm)
