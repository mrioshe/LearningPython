def armstrong(x):
    n=str(x)
    s=0
    for i in range(len(n)):
        s+=(int(n[i]))**len(n)
    if s==x:
        return True
    else:
        return False

'''if N<200:
    for i in range(N):
        a = input()
        b=int(a)
        #if b <100000:
            if armstrong(b):
                print(a,'es Armstrong')
            else:
                print(a,'no es Armstrong')'''
N=int(input())
for i in range(N):
    a = input()
    b=int(a)
    if armstrong(b):
        print(a,'es Armstrong')
    else:
        print(a,'no es Armstrong')               
        
    
