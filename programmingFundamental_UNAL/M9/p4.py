n=int(input())
if n <= 200:
    for i in range(n):
        a=input()
        b=a.split()
        if min(b)==b[0]:
            print( 'Mi cacharrito es el mas viejo de todos los autos ;D')
        else:
            print( 'Al menos otro auto es mas viejo que mi cacharrito :(')
