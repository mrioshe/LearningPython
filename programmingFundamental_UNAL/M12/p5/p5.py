a=open('discurso.txt','r')
dic={}

for renglones in a:
    b=renglones.replace(',','').replace('.','').replace(';','').replace(':','').replace('?','').replace('!','').replace('¡','').replace('¿','').lower().split()
    b=list(set(b))
    for k in range(len(b)):
        if len(b[k]) > 4:
            if b[k] in dic.keys():
                dic[b[k]]+=1
            else:
                dic[b[k]]=1

lista= list(dic.keys())
lista.sort()
for n in range(len(lista)):
    print(lista[n],dic[lista[n]])

a.close
