def f(x):
    if x%123==0:
        return 0
    else:
        return 1+f(x+23)
N=int(input())
for i in range(N):
    a=int(input())
    print(f(a))
