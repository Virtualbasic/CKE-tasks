with open("tekst.txt" , "r") as nm:
    for i in nm:
        ans = i.split()

    nm.close()

anserw= []
for i in range(len(ans)):
    for j in range(len(ans[i])-1):
        if  ans[i][j] == ans[i][j+1]:
            anserw.append(ans[i])
            break
print(anserw)
