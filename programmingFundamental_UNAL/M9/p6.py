C=int(input())
if C<=50:
    for i in range(C):
        a=input()
        #b=a.split()
        #if len(b)>1 and len(b)<=100:
        contadorf=a.count('F')
        contadorm=a.count('M')
        if contadorf==contadorm:
            print('Es posible hacer un unico circulo')
        else:
            print('No es posible')
