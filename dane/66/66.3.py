T = [i[:-1].split() for i in open("trojki.txt" , "r")]

for i in T:
    if int(i[0])**2 + int(i[1])**2 == int(i[2])**2:
        print(i)


