N=int(input())
dic_reggaeton={}
dic_rock={}
for k in range(N):
    l1=input().split()
    for i in range(len(l1)):
        if l1[i] in dic_reggaeton.keys():
            dic_reggaeton[l1[i]] += 1
        else:
            dic_reggaeton[l1[i]]= 1
M=int(input())
for h in range(M):
    l2=input().split()
    for j in range(len(l2)):
        if l2[j] in dic_rock.keys():
            dic_rock[l2[j]] += 1
        else:
            dic_rock[l2[j]]= 1
print('Reggaeton:',len(dic_reggaeton),'Rock:',len(dic_rock))
