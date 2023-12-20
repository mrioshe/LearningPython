def espejos(l):
    c=0
    for i in range(1,len(l)):
        l1=[]
        l2=[]  
        for j in range(i):
            l1.append(l[j])
        for k in range(i,len(l)):
            l2.append(l[k])
        if sum(l1)==sum(l2):
            c+=1
    return c
l=[]
N=int(input())
for i in range(N):
    l.append(float(input()))
print(espejos(l))
    
