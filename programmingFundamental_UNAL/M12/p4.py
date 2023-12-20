a=int(input())
for i in range(a):
    c=0
    lista=(input().split(' : '))
    l=[]
    for k in range(len(lista)):
        l.append(lista[k].replace(' ',''))
    if len(l[0])==len(l[1]):
        for j in range(len(l[0])):
            if l[0][j] in l[1]:
                c+=1
            else:
                break
    if c==len(l[0]):
        print('Es anagrama')
    else:
        print('No es anagrama')
    
            
