N=int(input())
for i in range (N):
    numeros=[]
    palos=[]
    for j in range(5):
        n=input()
        numeros.append(int(n))
        palos.append(input())
    numeros.sort()
    l=[]
    for k in range(numeros[0],numeros[0]+5):
        l.append(k)
    if l==numeros:
        if palos[0]==palos[1] and palos[0]==palos[2] and palos[0]==palos[3] and palos[0]==palos[4]:
            if l[0]==10:
                print('Escalera real')
            else:
                print('Escalera de color')
        else:
            print('Escalera normal')
    elif palos[0]==palos[1] and palos[0]==palos[2] and palos[0]==palos[3] and palos[0]==palos[4]:
        print('Color')
    else:
        print('Otra mano')
        
        
        
        
        
