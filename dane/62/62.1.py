with open("liczby1.txt" , "r")  as num:
    b = 0
    for i in num:
        n = int(i[:-1])
        break
    for i in num:
        if int(i[:-1]) > b:
            b = int(i[:-1])
        if int(i[:-1])<n:
            n = int(i[:-1])


num.close()
print(b)
print(n)