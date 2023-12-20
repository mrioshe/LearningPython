C= int(input())
for i in range(1,C+1):
    A = int(input())
    P= int(input())
    Q = int(input())
    s=A
    for k in range (P,Q+1):
        if s%k==0:
            s= s/k
            if k==Q:
                print(A, "es polifactor entre", P, "y", Q)
        else:
            print(A, "no es polifactor entre", P, "y", Q)
            break
     
