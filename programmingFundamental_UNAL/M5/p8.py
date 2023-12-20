W=float(input())
N=int(input())
S=0
n=0
for i in range(1,N+1):
    S += float(input())
    if S>W:
        continue
    n += 1
print(n)
