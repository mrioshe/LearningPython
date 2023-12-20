def alfa(X):
    m = X - 3
    return (3*[m])

def beta(Y):
    n = len(L)
    s = 0
    for e in L:
        s += e*n
        n -= 1

L = [6, 3, 10, 4, 9]
print(alfa(beta(L)))
