func = []
with open("funkcja.txt" , "r") as functions:
    for i in functions:
        temp = i[:-1].split()
        for i in range(len(temp)):
            temp[i] = float(temp[i])
        func.append(temp)
print(func)

equation =  (func[1][0]) + (func[1][1]*1.5) + (func[1][2] * (1.5**2)) + (func[1][3] * (1.5**3))

print(round(equation,5))

print(func)
x = 0
handler = []
zeropoint = []
for i in range(len(func)):
    for j in range(1, 1000):
        z = round((x + (j / 1000)), 3)
        eq = (func[i][0]) + (func[i][1]*z) + (func[i][2] * z) + (func[i][3] * (z**3))
        if eq == 0:
            zeropoint.append([round(eq,5),z])
        #print(round(eq,5) , end=f"{z}")
        handler.append([round(eq,5),z])
    x+=1
bgX = 0
acc = []
for i in range(len(handler)):
    if handler[i][0] > bgX:
        bgX = handler[i][0]
        acc = handler[i]
print(acc)
print(zeropoint)
a = round(func[0][0], 3)
b= round(func[0][1]*0.53656, 3)
c =round(func[0][2] * (0.53656**2), 3)
d = round(func[0][3] * (0.53656**3), 3)
#print(((func[0][0]) + (func[0][1]*0.53656) + (func[0][2] * (0.53656**2)) + (func[0][3] * (0.53656**3))))
print(a)
print(b)
print(c)
print(d)
print(round(a +b + c +d  , 3) )