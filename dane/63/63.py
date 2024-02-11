ciagi = []
ciagi2 = []
ciagi3 = []
def ifhalffirst(n):
    ifHfirst = False
    def iffirst(n):
        i = n-1
        flag = True
        while i>1:
            if n % i ==0:
                flag= False
                break
            i-=1
        return  flag
    first = []
    for i in range(n):
        if iffirst(i) and i!= 0 and i!= 1 :
            first.append(i)
    for i in range(len(first)):
        for j in range(i+1, len(first)-1):
            if i*j == n:
                ifHfirst = True
                break
    return  ifHfirst


with open("ciagi.txt" , "r") as ctg:
    for c in ctg:

        if len(c[:-1]) %2 ==0:
            left = int((len(c[:-1]) /2 ) )

            if c[:-1][left:] == c[:-1][:left]:
                ciagi.append(c[:-1])
        c += "0"
        flag = False
        for i in range(len(c[:-1])-1):
            if c[:-1][i] =="1" and  c[:-1][i+1] =="1":
                flag = True
                break
        if not flag:
            ciagi2.append(c[:-2])
        flag = False
        decC = int(c[:-2], 2)
        print(ifhalffirst(decC))
        if ifhalffirst(decC):
            ciagi3.append(decC)
        #print(c[:-2] , end=f" {  int(c[:-2], 2)} \n")
        #while i <decC:
        #    if
#63.1
#print(ciagi , end=f" {len(ciagi)}")
#63.2
#print(len(ciagi2))
#63.3
print(ciagi3)