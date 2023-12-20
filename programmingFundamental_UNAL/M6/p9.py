n=0
l=[]
while n<=2000:
    a=int(input())
    if a == 0:
        break
    l.append(a)   
    n +=1
b=0
if len(l)%2==0:
    for i in range(int(len(l)/2)):
        for j in range(len(l)):
            if i==j:
                continue
            if l[i]+l[j]==1995:
                b+=1
else:
    for i in range((len(l)//2)+1):
        for j in range(len(l)):
            if i==j:
                continue
            if l[i]+l[j]==1995:
                b+=1    
print(b)        
