with open("ciagi.txt" , "r") as sequence:
    tmp = [i[:-1] for i in sequence]
    out = []
    g = 0
    c = 0
    ar = 0
    while g<len(tmp)-1:
        out.append([int(tmp[g]), [int(i) for i in tmp[g+1].split()]])
        r = out[c][1][1] - out[c][1][0]
        if (out[c][1][0] + (r * (out[c][0]-1))) == out[c][1][len(out[c][1])-1]:
            print(r , end=f" {(r * (out[c][0]-1))}\n")
            ar+=1
            #print("arytmetyczny")
        g+=2
        c+=1

print(out)
print(ar)

