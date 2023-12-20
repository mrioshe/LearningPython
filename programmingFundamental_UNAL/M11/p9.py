from datetime import datetime, timedelta
dic={}
C=int(input())
for i in range(C):
    #print('\n')
    dic['Monday']=['lun\t']
    dic['Tuesday']=['mar\t']
    dic['Wednesday']=['mie\t']
    dic['Thursday']=['jue\t']
    dic['Friday']=['vie\t']
    dic['Saturday']=['sab\t']
    dic['Sunday']=['dom']
    d=input()
    dd='01'+d[2:]
    mes=int(dd[3:5])
    if mes<12:
        dd2='01/'+str(mes+1)+dd[5:]
    else:
        dd2='01/01/'+str(int(int(dd[6:])+1))
    n_days= (datetime.strptime(dd2,'%d/%m/%Y')-datetime.strptime(dd,'%d/%m/%Y')).days
    
    if datetime(int(d[6:]),int(mes),1).strftime('%A')== 'Sunday':
        dic['Monday'].append('\t')
        dic['Tuesday'].append('\t')
        dic['Wednesday'].append('\t')
        dic['Thursday'].append('\t')
        dic['Friday'].append('\t')
        dic['Saturday'].append('\t')
    elif datetime(int(d[6:]),int(mes),1).strftime('%A')== 'Saturday':
        dic['Monday'].append('\t')
        dic['Tuesday'].append('\t')
        dic['Wednesday'].append('\t')
        dic['Thursday'].append('\t')
        dic['Friday'].append('\t')
    elif datetime(int(d[6:]),int(mes),1).strftime('%A')== 'Friday':
        dic['Monday'].append('\t')
        dic['Tuesday'].append('\t')
        dic['Wednesday'].append('\t')
        dic['Thursday'].append('\t')
    elif datetime(int(d[6:]),int(mes),1).strftime('%A')== 'Thursday':
        dic['Monday'].append('\t')
        dic['Tuesday'].append('\t')
        dic['Wednesday'].append('\t')
    elif datetime(int(d[6:]),int(mes),1).strftime('%A')== 'Wednesday':
        dic['Monday'].append('\t')
        dic['Tuesday'].append('\t')
    elif datetime(int(d[6:]),int(mes),1).strftime('%A')== 'Tuesday':
        dic['Monday'].append('\t')
        
    for k in range(1,n_days+1):
        dic[datetime(int(d[6:]),int(mes),k).strftime('%A')].append(str(k)+'\t')
    n=max(len(dic['Monday']),len(dic['Tuesday']),len(dic['Wednesday']),len(dic['Thursday']),len(dic['Friday']),len(dic['Saturday']),len(dic['Sunday']))

    for z in range(1,len(dic['Sunday'])):
        dic['Sunday'][z]=dic['Sunday'][z][:-1]
       
    if datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Monday':
        dic['Tuesday'].append('\t')
        dic['Wednesday'].append('\t')
        dic['Thursday'].append('\t')
        dic['Friday'].append('\t')
        dic['Saturday'].append('\t')
        dic['Sunday'].append('\t')
    elif datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Tuesday':
        dic['Wednesday'].append('\t')
        dic['Thursday'].append('\t')
        dic['Friday'].append('\t')
        dic['Saturday'].append('\t')
        dic['Sunday'].append('\t')
    elif datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Wednesday':
        dic['Thursday'].append('\t')
        dic['Friday'].append('\t')
        dic['Saturday'].append('\t')
        dic['Sunday'].append('\t')
    elif datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Thursday':
        dic['Friday'].append('\t')
        dic['Saturday'].append('\t')
        dic['Sunday'].append('\t')
    elif datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Friday':
        dic['Saturday'].append('\t')
        dic['Sunday'].append('\t')
    elif datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Saturday':
        dic['Sunday'].append('\t')

    for j in range(n-1):
        print(dic['Monday'][j]+dic['Tuesday'][j]+dic['Wednesday'][j]+dic['Thursday'][j]+dic['Friday'][j]+dic['Saturday'][j]+dic['Sunday'][j])

    if datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Monday':
        print(dic['Monday'][-1][:-1])
    elif datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Tuesday':
        print(dic['Monday'][-1]+dic['Tuesday'][-1][:-1])
    elif datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Wednesday':
        print(dic['Monday'][-1]+dic['Tuesday'][-1]+dic['Wednesday'][-1][:-1])
    elif datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Thursday':
        print(dic['Monday'][-1]+dic['Tuesday'][-1]+dic['Wednesday'][-1]+dic['Thursday'][-1][:-1])
    elif datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Friday':
        print(dic['Monday'][-1]+dic['Tuesday'][-1]+dic['Wednesday'][-1]+dic['Thursday'][-1]+dic['Friday'][-1][:-1])
    elif datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Saturday':
        print(dic['Monday'][-1]+dic['Tuesday'][-1]+dic['Wednesday'][-1]+dic['Thursday'][-1]+dic['Friday'][-1]+dic['Saturday'][-1][:-1])
    elif datetime(int(d[6:]),int(mes),n_days).strftime('%A')== 'Sunday':
        print(dic['Monday'][-1]+dic['Tuesday'][-1]+dic['Wednesday'][-1]+dic['Thursday'][-1]+dic['Friday'][-1]+dic['Saturday'][-1]+dic['Sunday'][-1])
    
    print('\r')

