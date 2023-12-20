h=int(input())
m=int(input())
if m==0 and h==12:
    print(12,':',0, sep='')
elif m==0:
    print(12-h,':',0, sep='')
elif h==11:
    print(12,':',60-m, sep='')
elif h !=12:
    print(11-h,':',60-m, sep='')
elif h==12:
    print(11,':',60-m, sep='')
    
