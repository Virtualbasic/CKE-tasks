def station(path , numsystem):
    reads = []
    with open(path , "r") as  red:
        for i in red:
            reads.append(i[:-1].split(" "))
    accbgc = [1 , 0]
    for z in range(len(reads)):
        reads[z] = [int(reads[z][0] , numsystem) , int(reads[z][1] , numsystem) ]
        if accbgc[1]> reads[z][1]:
            accbgc =reads[z]
    print(accbgc)
    return [bin(accbgc[0]) , bin(accbgc[1])]
print(station("dane_systemy1.txt" , 2), end="s1 \n")
print(station("dane_systemy2.txt" , 4), end="s2 \n")
print(station("dane_systemy3.txt" , 8), end="s3 \n")