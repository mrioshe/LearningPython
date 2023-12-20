V = int(input())
E = int(input())
print(E-V)
if (((E-V)%10==0 or (E-V)%15==0) and (E-V)%4!=0 ):
    print('y te lo puedes quedar')
