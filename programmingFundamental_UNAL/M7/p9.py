def perfecto(x):
    l=[]
    for i in range(1,x):
        if x%i==0:
            l.append(i)
    if sum(l)==x:
        return True
    else:
        return False
N=int(input())
if N<200:
    for i in range(N):
        a=int(input())
        if perfecto(a):
            print(a,'es perfecto')
        else:
            print(a,'no es perfecto')
