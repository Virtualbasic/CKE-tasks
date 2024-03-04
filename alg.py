ile = {}
def alg(N):
    d=2
    while N>=d:
        if N%d ==0:
            if d in ile:
                ile[d]+=1
            else:
                ile[d]=1
            print(d)
            N= N//d
        else:
            d+=1

alg(784)
print(ile)
#print(len(ile))
'''
d ← 2
T ← {}
dopóki N>=d wykonuj 
    jeżeli (N mod d ) = 0 to
        N ← N div d
        jeżeli d w T
            T[d] ←  T[d] + 1 
        w przeciwnym razie
            T[d] ← 1

'''



'''
36 
2
2
3
3
120
2
2
2
3
5
675
3
3
3
5
5

b)

czynniki pierwsze liczby N
c)
100
'''
