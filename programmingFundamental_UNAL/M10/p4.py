N=int(input())
dic={}
if N<=1000:
    for i in range(N):  
        a=(input().split())
        dic[a[0]]=a[1]
M=int(input())
if M <=500:
    for j in range(M):
        m=input()
        if m in dic.keys():
            print(dic[m])
        else:
            print('palabra no encontrada')
        
    
    
