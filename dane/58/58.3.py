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
    recordRecords = 0
    subrec1 = [reads1[0][1]]
    subrec2 = [reads2[0][1]]
    subrec3 = [reads3[0][1]]
    for i in range(1,len(reads1)):
        acc = [int(reads1[i][1]) , int(reads2[i][1]) , int(reads3[i][1]) ]
        #print(acc)
        subrec1 =sorted(subrec1)[::-1]
        subrec2 =sorted(subrec2)[::-1]
        subrec3 = sorted(subrec3)[::-1]

        if acc[0]>subrec1[0] or acc[1]>subrec2[0]  or acc[2]>subrec3[0]:
                recordRecords +=1

        subrec1.append(int(reads1[i][1]))
        subrec2.append(int(reads2[i][1]))
        subrec3.append(int(reads3[i][1]))
    return  recordRecords+1 # dlatego że uwzględniamy pierwszy rekord jako ekstremum , bo w tablicy wtedy są tylko jedne liczby
print(station("dane_systemy1.txt" ,"dane_systemy2.txt" ,"dane_systemy3.txt" , 2, 4 ,8))