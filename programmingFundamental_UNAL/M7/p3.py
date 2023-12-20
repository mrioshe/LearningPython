c=299792458 
def gamma(v):
    k=1/(1-(v**2/c**2))**(1/2)
    return k

N=int(input())
for i in range(N):
    v=float(input())
    if v*10/36 <= c:
        print(round(gamma(v*10/36),15))
