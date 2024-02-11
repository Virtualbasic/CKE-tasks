with open("napisy.txt" , "r") as nm:
    endings = []
    for i in nm:
        tmp = i.split()
        end = ""
        left= len(tmp[0])
        right = len(tmp[1])
        n= 0
        if left> right:
            g = left
        else:
            g= right
        while n < g:
            one = tmp[0][::-1]
            two = tmp[1][::-1]
            if one[n] == two[n]:
                end+= one[n]
            else:
                    endings.append([end[::-1] , tmp])
                    break
            n+=1
    nm.close()
    print(endings)
bg =  0
acc = []
for i in endings:
    if len(i[0])>bg:
        bg = len(i[0])
        acc = i
for i in endings:
    if len(i[0]) ==bg:
        acc.append(i)
print(acc)