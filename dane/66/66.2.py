T = [i[:-1].split() for i in open("trojki.txt" , "r")]
def czypeirw(x):
    n = 2
    while n<int(x):
        if  int(x)%n ==0 :
            return False
        n+=1
    return  True

for i in T:
    if czypeirw(i[0]) and czypeirw(i[1]) and int(i[0])*int(i[1]) == int(i[2]):
        print(i , end=f" {int(i[0])*int(i[1])}  = {int(i[2])} \n")

