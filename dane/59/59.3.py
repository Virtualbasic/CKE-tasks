
def moc(x):
    m = 0
    l = len(str(x))
    while l !=1:
        p = 1
        for i in str(x):
            p *= int(i)
        x = str(p)
        l = len(x)
        m+=1

    return m

liczby = [int(i[:-1]) for i in open("liczby.txt" , 'r')]

biggest = 0
smallest = liczby[0]
dict = {k:0 for k in  range(1,9) }


warunek = []
for i in liczby:
    if moc(i) <= 8 and moc(i) !=0:
        dict[moc(i)] +=1
    if moc(i) == 1 and i> biggest:
        biggest = i
    if moc(i) == 1  and i<smallest:
        smallest = i
print(len(warunek))
print(dict)
print(f"{smallest} \n")
print(biggest)

