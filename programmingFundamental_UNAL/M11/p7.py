from random import sample
p=int(input())
for i in range(p):
    l= 4*list(range(1,14))
    l_plataforma=input().split()
    c1=0
    c2=0
    l1=sample(l,k=13)
    for z in range(len(l_plataforma)):
        if l1[z]> int(l_plataforma[z]):
            c1+=1
        elif int(l_plataforma[z])> l1[z]:
            c2 +=1
    
    print('Puntos humano:',c1,'Puntos plataforma:',c2)
