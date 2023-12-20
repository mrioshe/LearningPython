def divisores(x):
    div=[]
    for i in range(x):
        if x%(i+1)==0:
            div.append(i+1)
    return div
  
j=[1]
while j[-1] < 10000:
    d=divisores(j[-1])
    j.append(len(d)+j[-1])  
for k in range(500):
    a=int(input())
    if k !=0 and a==0:
        break
    if a>0 and a<10000:
        if a in j:
            print('Pertenece a la serie de Julianachi')
        else:
            print('No pertenece a la serie de Julianachi')
