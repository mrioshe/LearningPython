from datetime import datetime, timedelta
R=int(input())
dic={}
for i in range(R):
    l=[]
    l=input().split()
    t=int(l[1][0:2])
    if t >=0 and t <= 3:
        if 'true vampires' in dic:
            dic['true vampires']+= 1
        else:
            dic['true vampires']= 1
    if t >=4 and t<= 7:
        if 'early birds' in dic:
            dic['early birds']+= 1
        else:
            dic['early birds']= 1
    if t >=8 and t<= 11:
        if 'sunny warmers' in dic:
            dic['sunny warmers']+= 1
        else:
            dic['sunny warmers']= 1
    if t >=12 and t<= 15:
        if 'lunch workers' in dic:
            dic['lunch workers']+= 1
        else:
            dic['lunch workers']= 1
    if t >=16 and t<= 19:
        if 'sunset lovers' in dic:
            dic['sunset lovers']+= 1
        else:
            dic['sunset lovers']= 1
    if t >=20 and t<= 23:
        if 'prime timers' in dic:
            dic['prime timers']+= 1
        else:
            dic['prime timers']= 1
if 'true vampires' in dic:
    print('true vampires',dic['true vampires'])
else:
    print('true vampires',0)
    
if 'early birds' in dic:
    print('early birds',dic['early birds'])
else:
    print('early birds',0)
if 'sunny warmers' in dic: 
    print('sunny warmers',dic['sunny warmers'])
else:
    print('sunny warmers',0)
if 'lunch workers' in dic:
    print('lunch workers',dic['lunch workers'])
else:
    print('lunch workers',dic['lunch workers'])
if 'sunset lovers' in dic:
    print('sunset lovers',dic['sunset lovers'])
else:
    print('sunset lovers',0)
if 'prime timers' in dic:   
    print('prime timers',dic['prime timers'])
else:
    print('prime timers',0)
