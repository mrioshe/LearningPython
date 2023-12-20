n=0
l=[]
while n<5000:
    a=int(input())
    if a == 0:
        break
    l.append(a)   
    n +=1
for i in range(len(l)):
    if  i+1 in l:
        continue
    else:
        break
print('La ficha faltante es la',i+1)
