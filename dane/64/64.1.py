pictures = []
with open("dane_obrazki.txt" , "r") as pic:
    temp = []
    for i in pic:
        if  i.isspace():
            pictures.append(temp[:-1])
            temp = []
        else:
            temp.append(i[:-2])

print(len(pictures))
counter = 0
for  i in pictures:
    temp = "".join(i)
    z = 0
    o = 0
    for j in temp:
        if j  == "0":
            z += 1
        else:
            o+=1
    if o > z:
        counter+=1
print(counter)