from datetime import datetime, timedelta
C=int(input())
for i in range(C):
    l=input().split()
    days=(datetime.strptime(l[1],'%d-%m-%Y')-datetime.strptime(l[0],'%d-%m-%Y')).days
    dx5=days//5
    dx1=days%5
    string=dx5*'5 '+dx1*'1 '
    print(string[:-1])
