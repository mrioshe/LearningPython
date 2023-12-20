E=int(input())
l=[]
for i in range(E):
    l.append(input().split(','))
for j in range(len(l)):
    l[j].append(round(float(l[j][1])/(float((l[j][2]))**2),1))
    if l[j][-1]> 25 and float(l[j][3])>100 and float(l[j][4])>150:
        l[j].append(True)
    else: 
        l[j].append(False)
l2=[]
for k in range(len(l)):
    l2.append([])
    if l[k][-1]==True:
        l2[k].append(l[k][-2])
        l2[k].append(l[k][0])
l2.sort(reverse=True)
c=1
for h in range(len(l2)):
    if not l2[h]==[]:
        print(c,l2[h][1],l2[h][0])
        c+=1            
    
