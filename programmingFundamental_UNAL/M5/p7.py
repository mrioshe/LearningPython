N=int(input())
l=float(input())
l_1=float(input())
A=0
for i in range (1,N+1):
    A +=l**2
    l +=l_1
print('El area total es de',A,'metros cuadrados')
