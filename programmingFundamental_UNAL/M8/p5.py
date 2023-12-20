N=int(input())
l=[]
for i in range(N):
    l.append(float(input()))
l1=l.copy()
l1.sort()
for k in range(N):
    print(l.index(l1[k])+1)
