l=[]
l.append(1)
c=0
while l[c]<=10000:
    c += 1
    l.append(c*(c+1)/2)
n=1
while n>0 and n<=500:
    a=int(input())
    if a==0:
        break
    elif a>0 and a <= 10000:
        if a in l:
            print('Puede ser un racimo ideal')
        else:
            print('No puede ser un racimo ideal')
    n += 1
            
