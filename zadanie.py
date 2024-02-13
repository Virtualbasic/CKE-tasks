

def z(tab , x):
    W = 0
    i = 0
    while i <= 4:
        sk =tab[i]
        j = 4 - i
        while j > 0 :
            sk *= x # 10  *
            j -= 1
        W += sk # 5 +
        i+=1 #
    return W
tab = [1,3,2,7,8]
x = 5
print(z(tab , x))

def z2(tab ,x):
    W = tab[0]
    i = 0
    while i <4:
        i += 1
        W  = (W*x) +tab[i]

    return  W
#((x * a0 + a1)  + a2 *x)

'''
W<-a0, i<-0
dopóki i<4 wykonuj:
    i <- i+1
    W <- (W*x) + ai
4 *
4 + 
'''
print(z2(tab,x))

# a