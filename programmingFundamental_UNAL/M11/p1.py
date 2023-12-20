from datetime import datetime, timedelta
C=int(input())
for i in range(C):
    l=[]
    l=input().split()
    t=datetime.strptime(l[2],'%Y-%m-%d')-datetime.strptime(l[1],'%Y-%m-%d')
    print(t.days,'dias =',t.days*24,'horas =',t.days*1440,'minutos =',t.days*86400,'segundos')
