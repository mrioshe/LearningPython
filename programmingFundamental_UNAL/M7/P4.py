def f(x):
    return((2+5*x)**(1/2))
def g(x):
    return((4+x)**3)
c=0
while c < 1000:
    a=int(input())
    if a==0:
        break
    else:
        if a%2==0:
            print(f(g(a)))
        else:
            print(g(f(a)))
    c += 1
