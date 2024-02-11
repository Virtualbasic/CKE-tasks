with open("napisy.txt" , "r") as nm:
    for i in nm:
        result = []
        tmp = i.split()
        if len(tmp[0]) > len(tmp[1]):
            check = tmp[0][len(tmp[1]):]
            if tmp[1]+ check == tmp[0]:
                print(f"napisy {tmp} , znaki jakie trzeba napisać {check}")
        else:
            check = tmp[1][len(tmp[0]):]
            if tmp[0] + check == tmp[1]:
                print(f"napisy {tmp} , znaki jakie trzeba napisać {check}")


