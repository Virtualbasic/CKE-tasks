#def checkschema(path , system)
#def binn(num):
#    binnum = ''
#    if num ==1:
#        return 1
#    while  num >0:
#        if num %2 == 0:
#            binnum += "0"
#        else:
#            binnum+="1"
#        num //= 2
#    return binnum[::-1]

#print(binn(256))
#print(int("100000000", 2))


def station(path , path2 , path3, numsystem , numsystem2 , numsystem3):
    reads1 = []
    reads2 = []
    reads3 = []
    with open(path , "r") as  red:
        for i in red:
            reads1.append(i[:-1].split(" "))
    with open(path2, "r") as red:
        for i in red:
            reads2.append(i[:-1].split(" "))
    with open(path3, "r") as red:
        for i in red:
            reads3.append(i[:-1].split(" "))

    for z in range(len(reads1)):
        reads1[z] = [int(reads1[z][0], numsystem), int(reads1[z][1], numsystem)]
        reads2[z] = [int(reads2[z][0], numsystem2), int(reads2[z][1], numsystem2)]
        reads3[z] = [int(reads3[z][0], numsystem3), int(reads3[z][1], numsystem3)]
    print(reads1)
    print(reads2)
    print(reads3)
    timer = int(reads1[0][0])
    readsFaults = 0
    for i in range(len(reads1)):
        if int(reads1[i][0])!=timer and int(reads2[i][0])!=timer and int(reads3[i][0])!=timer:
            readsFaults+=1
        timer+=24
    return readsFaults

print(station("dane_systemy1.txt" ,"dane_systemy2.txt" ,"dane_systemy3.txt" , 2, 4 ,8))
