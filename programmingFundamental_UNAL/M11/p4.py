from datetime import datetime, timedelta
C=int(input())
for i in range(C):
    l=input()
    t=datetime.strptime(l,'%I:%M:%S %p')
    s=round(100*(t.hour*3600+t.minute*60+t.second)/86400,3)
    print('Loading day ... ',s,'%',sep='')
    
    
