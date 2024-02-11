def station(path , numsystem):
    reads = []
    with open(path , "r") as  red:
        for i in red:
            reads.append(i[:-1].split(" "))
    temperature_jumps =[]
    for z in range(len(reads)):
        reads[z] = [int(reads[z][0] , numsystem) , int(reads[z][1] , numsystem) ]
    zindex = 0
    secindex = 0
    print(reads)
    for x in range(len(reads)):
        z = x+1

        for i in range(z,len(reads)):

            f = reads[x][1]
            sec = reads[z][1]
            if f ==0 or sec == 0:
                secindex+=1
            else:
                print(z)
                print(x)
                temperature_jumps.append(((f -sec )**2)/((zindex-secindex)*-1))
                secindex+=1
        zindex+=1
    return  temperature_jumps

print(station("dane_systemy1.txt" , 2), end="s1 \n")