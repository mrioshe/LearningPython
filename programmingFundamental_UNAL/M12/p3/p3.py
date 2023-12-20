a=open('matrix.txt','r')
lista=[]

for renglones in a:
    if renglones[0:6]=='Smith:':
        b=renglones.replace('?','_?_').split('?')
        for j in range(1,len(b),2):
            if b[j] not in lista:
                lista.append(b[j])

for g in range(len(lista)):
    print('?'+lista[g][1:-1]+'?')


a.close

