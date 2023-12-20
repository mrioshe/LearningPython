def funcionA(N):

    return N*4

 

def funcionB(N):

    return N**2

 

def funcionC(N):

    N -= 6

 

N = 6

X = funcionA(N)

N += funcionB(N)

funcionC(N)

print(N)
