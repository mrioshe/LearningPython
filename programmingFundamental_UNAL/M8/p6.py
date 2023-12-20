def multidigito(x):
    n=str(x)
    l=[]
    for i in range(len(n)):
        l.append(n[i])
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0

    for i in range(len(n)):
        if l[i]=='1': 
            c1 +=1
        if l[i]=='2': 
            c2 +=1
        if l[i]=='3': 
            c3 +=1
        if l[i]=='4':
            c4 +=1
        if l[i]=='5': 
            c5 +=1          
    if c1>=1 and c2>=1 and c3>=1 and c4>=1 and c5>=1:
        return True
    else:
        return False
N=0
while N<=100:
    a=int(input())
    if a>0:
        if multidigito(a):
            print('Multidigito')
        else:
            print('No es multidigito')
    elif a==0:
        break
    N +=1

    
