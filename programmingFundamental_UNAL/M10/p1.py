N = int(input())
l=[]
l2=[]
if N <=1000:
    for n in range(N):
        l.append(input().split())
    for i in range(len(l)):
        if l[i][2]=='positiva':
            l2.append(l[i])
    l3=[]
    for k in range(len(l2)):
        l3.append([])
        a=l2[k][1]
        b=l2[k][2]
        c=l2[k][3]
        l3[k].append(int(c))
        l3[k].append(int(a))
        l3[k].append(b)
    l3.sort(reverse=True)
    for j in range(len(l3)):
        print(l3[j][1],(l3[j][2]).upper(),l3[j][0])
  
    
