def P(x):
    return 2*x+1
def A(x):
    return 3**x
def N(x):
    return (5*x+4)**(1/2)
c = int(input())
for i in range(c):
    a=float(input())
    print(P(A(N(a))))
