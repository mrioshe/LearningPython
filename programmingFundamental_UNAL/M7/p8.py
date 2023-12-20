import sys
sys.setrecursionlimit(10**5)
def A(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A(m-1,1)
    elif m>0 and n>0:
        return A(m-1,A(m,n-1))
m = int(input())
n=int(input())
if (m>=0 and m<=3) and(n>=0 and n<=8):
    print(A(m,n))
      
