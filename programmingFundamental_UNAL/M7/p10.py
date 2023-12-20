import math
def fuertes(x):
    n=str(x)
    l=[]
    for i in range(len(n)):
        l.append(int(n[i]))
    s=0
    for i in range(len(l)):
        s+= math.factorial(l[i])
    if s== x:
        return True
    else:
        return False
N=int(input())
if N <= 200:
    for i in range(N):
        a=int(input())
        if fuertes(a):
            print(a,'es fuerte')
        else:
            print(a,'no es fuerte')
