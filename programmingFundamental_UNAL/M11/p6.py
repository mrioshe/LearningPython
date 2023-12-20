from datetime import datetime, timedelta
c=int(input())
for i in range(c):
    l=[]
    k=0
    l=input().split()
    year=int(l[0][0:4])+1
    for z in range(int(l[1])):
        fecha= str(year)+l[0][4:]
        t=datetime.strptime(fecha,'%Y/%m/%d')
        if t.strftime('%A')== 'Monday':
            k+=1
        year+=1
    print(k)
