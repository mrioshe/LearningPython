N=int(input())
numero_ejericios=[9,11,12,8,12,9,11,8,11,10,9,10]
l=[]
l2=[]
for i in range(N):
    l.append(input().split(','))
for k in range(len(l)):
    l2.append([])
    for j in range(12):
        l2[k].append(round(int(l[k][1+j])*5/numero_ejericios[j],1))
l3=[]
for j in range(len(l2)):
    l3.append(round(sum(l2[j])/12,1))
l4=[]
for g in range(len(l2)):
    l4.append([l[g][0],l3[g]])
l4.sort()
for f in range(len(l)):
    print(l4[f][0],l4[f][1])
    
    
    
        
        
