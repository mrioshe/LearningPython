C=int(input())
for i in range(C):
    control=True
    l=[]
    N=int(input())
    for j in range(N):
        lista=input().split()
        l.append(lista[0])
        l.append(lista[1])
    l2=list(set(l))
    for k in range(len(l2)):
        if l.count(l2[k]) != 2:
            control = False
    if control== True:
        print('Volvieron a C-137')
    else:
        print('Deambulan por el multiverso')
