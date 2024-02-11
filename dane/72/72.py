with open("napisy.txt" , "r") as nm:
    result = []
    c = 0
    for i in nm:
        tmp  = i.split()
        if len(tmp[0]) >= len(tmp[1]) *3 or len(tmp[1]) >= len(tmp[0])*3:
            result.append(tmp)
    print(result[0] , end=f" {len(result)}")
    nm.close()
