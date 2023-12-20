N=int(input())
if N <=100:
    for i in range(N):
        a=input()
        b=a.split('_')
        s=''
        for k in range(len(b)):
            s = s+b[k].capitalize()
        print(s)
             
    
