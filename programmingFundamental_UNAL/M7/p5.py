def hyperpar(x):
    c=0
    for i in range(len(x)):
        if (int(x[i])%2)!=0:
            c=1
            break
    if c==0:
        return True
    elif c==1:
        return False
k=0
while k < 500:
    a=input()
    if a=='-1':
        break
    else:
        if hyperpar(a)== True:
            print('Hyperpar')
        else:
            print('No es hyperpar')
    k=k+1
