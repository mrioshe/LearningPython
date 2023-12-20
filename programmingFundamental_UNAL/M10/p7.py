N=int(input())
if N<=5000:
    dic={}
    for i in range(N):
        a=input().split(':')
        if a[0] in dic.keys():
            dic[a[0]]= dic[a[0]]+ int(a[1])
        else:
            dic[a[0]]=int(a[1])
    print('El vendedor del mes es',max(dic, key=dic.get))
