N = int(input())
M = int(input())
l=[]
l2=[]
l3=[]
for i in range(M):
    l2.append(input())
    
for i in range(N):
    l.append(l2.count(str(i+1)))
    
for i in range(N):
    if l[i]== max(l):
        l3.append(i+1)
        
for i in range(len(l3)):
    print(l3[i])
