N=int(input())
l1=[]
l2=[]
for i in range(N):
    l1.append(input())
for i in range(N):
    l2.append(input())
a=0
b=0
for i in range (N):
    if l1[i]>l2[i]:
        a +=2
    elif l1[i]<l2[i]:
        b +=2
    else:
        a +=1
        b +=1
print('Ballenota Futbol Club:', a)
print('Real Mandril:', b)
        
        
