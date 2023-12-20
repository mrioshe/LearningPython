def bandera(L):
    l1=[]
    for n in range(L):
        l1.append([])
        for b in range(L):
            l1[n].append('0')
    for k in range(L):
        l1[k][int((L-1)/2)]='+'
    for p in range(L):
        l1[int((L-1)/2)][p]='+'
    for f in range(L):
        for m in range(L):
            if f == m or m+f==L-1 :
                l1[m][f]='#'
    l2=[]
    for z in range(L):
        l2.append(''.join(l1[z]))
    return(l2)
        
C=int(input())
if C < 50:
    for i in range(C):
        l=int(input())
        lista=[]
        for j in range(l):
            lista.append(str(input()))
        if lista==bandera(l):
            print('Bandera britanica')
        else:
            print('Ni idea')
            
