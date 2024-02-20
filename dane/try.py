s = ["213asd2" , "dsadsa2131" , "213213132", "dfadasd21"]

def zx(x):
    for g in  x:
        if not g.isnumeric():
            return  False
    return True

for i in s:
    try:
        if int(i):
            print(i)
    except:
        pass