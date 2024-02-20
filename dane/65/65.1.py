numbers = [i[:-1].split() for i in open("dane_ulamki.txt" , "r")]
ulamki = []

for i in numbers:
    i[0], i[1] = int(i[0]), int(i[1])
    ulamki.append([i , i[0]/i[1]])

nmmian = ulamki[0][0][1]
nmnum = ulamki[0][1]
handler = []
for i in range(len(ulamki)):
    if ulamki[i][1] < nmnum:
        nmnum = ulamki[i][1]
        handler = ulamki[i][0]

print(nmnum)
print(handler)