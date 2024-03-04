with open("hasla.txt" , "r") as pas:
    c = 0
    passwords = {}
    specpasswords = []
    fourchars = []
    for i in pas:
        f1=False
        f2=False
        f3=False
        fisascii=False
        sub1 = ""
        sub2 = ""
        sub3 = ""
        if i[:-1] in passwords:
            passwords[i[:-1]]+=1
        else:
            passwords[i[:-1]] = 1
        if i[:-1].isnumeric():
            #print(i)
            c+=1
        for j in i:
            if j.isnumeric():
                sub1+=j
                sub2+="_"
                sub3+="_"
                f1 = True
            if j.isupper():
                sub1 +=  "_"
                sub2 += j
                sub3 += "_"
                f2 = True
            if j.islower():
                sub1 += "_"
                sub2 += "_"
                sub3 += j
                f3 = True

        if f1 and f2 and f3:
            specpasswords.append(i[:-1])
        c1 = 0 # numbers
        c2 = 0 # uppers
        c3 = 0 # lowers
        for g in range(len(sub1)):
            print(sub1)
            print(sub2)
            print(sub3)
            if sub1[g] == "_":
                c1= 0
            if sub2[g] =="_":
                c2= 0
            if sub3[g] == "_":
                c3 =0
            if c1 == 4 or c3==4  or c2==4:
                fourchars.append(i[:-1])
                break
            c1+=1
            c2+=1
            c3+=1

    #1
    #print(c)
    #2
    #print(passwords)
    #print([(k, v) for k ,v in passwords.items() if v >=2] )
    #3
    print(fourchars)
    print(len(fourchars))
    #4
    #print(specpasswords)
    #print(len(specpasswords))
    pas.close()