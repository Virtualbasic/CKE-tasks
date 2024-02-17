with open("hasla.txt" , "r") as n:
    onlynumeric = []
    for i in n:
        flaga = False
        try:
            if int(i[:-1]):
                flaga = True
        except:
            pass
        finally:
            if flaga:
                onlynumeric.append(i[:-1])
    print(onlynumeric)