def lucas(x):
    l=[2,1]
    while l[-1]<=x:
        l.append(l[-1]+l[-2])
    if l[-1]!=[-2]:
        l.pop(-1)
    return l
A=int(input())
B=int(input())
l1=lucas(A)
l2=lucas(B)
if A in l1 or B in l2:
    print(abs(len(lucas(A))-len(lucas(B)))+1)
else:
    print(abs(len(lucas(A))-len(lucas(B))))
