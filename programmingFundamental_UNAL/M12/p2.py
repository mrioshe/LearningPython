from datetime import datetime, timedelta
R=int(input())
l=[]
for i in range(R):
    l.append(input())
s=0
for k in range(1,len(l)):
    t1=datetime.strptime(l[k],'%Y-%m-%d %H:%M:%S')-datetime.strptime(l[k-1],'%Y-%m-%d %H:%M:%S')
    s+=(t1.seconds + (t1.days)*86400)
t=s/(len(l)-1)
print(int(t//86400),'dias,',int((t%86400)//3600),'horas,',int(((t%86400)%3600)//60), 'minutos,',int(((t%86400)%3600)%60),'segundos')



