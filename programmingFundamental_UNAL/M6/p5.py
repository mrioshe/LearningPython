N=int(input())
l1=[]
l2=[]
for i in range(N):
    l1.append(int(input()))
for i in range(N):
    l2.append(int(input()))
c=0
l1.sort()
l2.sort(reverse=True)
for i in range(N):
    if (l1[i])%2!=(l2[i])%2:
        c += 2
print('Sobreviven',c, 'soldados')
