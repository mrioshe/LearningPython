N = int(input())
V=0
for i in range(1,N+1):
    a=i*float(input())-V
    print(int(a))
    V += a
