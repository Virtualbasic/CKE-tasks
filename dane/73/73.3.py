with open("tekst.txt" , "r") as text:
    words = []
    for i in text:
        ans = i.split()
    for i in range(len(ans)):
        print(ans[i])
        flag = False
        for j in ans[i]:
            if j  in "AEIOUY":
                flag=True
                break
        print(flag)
        if flag:
            words.append(ans[i])
    text.close()
print(words)
print(len(words))
