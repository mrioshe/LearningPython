from datetime import datetime, timedelta
r=int(input())
c=0
t=0
for i in range(r):
    l=[]
    l=input().split(', ')
    if l[1]=='barberia':
        t1=datetime.strptime(l[3],'%H:%M:%S')-datetime.strptime(l[2],'%H:%M:%S')
        t=t+t1.seconds
        c+=1
print(c, 'veces')
tt=t//c
print(tt//3600,'horas,',(tt%3600)//60, 'minutos,',(tt%3600)%60,'segundos')
