'''def bandera_escosesa(x):
    l=[]
    for i in range(x):
        for j in range(x):
            l.append('0')
        l[i],l[-(i+1)]='#','#'
        for k in range(x):
        return sum(l)   
while True:
    l1=int(input())
    if l1==0:
        break
    else:
        if l1 >3 and l1<20:
            print(bandera_escosesa(l1))'''

while True:
    a=int(input())
    if a==0:
        break
    else:
        if  a >2 and a<20:          
            for i in range(a):
                l=[]
                for j in range(a):
                    l.append('0')
                l[i],l[-(i+1)]='#','#'
                s=''
                for i in range(a):
                    s= s+l[i]
                print(s)
                    
                    
 
