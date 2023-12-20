N = int(input())
if N==3:
    print('El numero 3 es el mejor')
elif N%3==0:
    print('El numero', N ,'es multiplo de 3. Y el numero 3 es el mejor')
else:
    if N%3==2:
        print('El numero', N, 'no es multiplo de 3, pero si le sumas 1 el resultado si lo es. Y el numero 3 es el mejor')
    else:
        print('El numero', N, 'no es multiplo de 3, pero si le restas 1 el resultado si lo es. Y el numero 3 es el mejor')
