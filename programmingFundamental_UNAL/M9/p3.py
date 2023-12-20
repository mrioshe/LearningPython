n=int(input())
if n<5000:
    for i in range(n):
        a=input()
        if a[-2]+a[-1]=='ix':
            print('Galo')
        elif a[-2]+a[-1]=='us':
            print('Romano')
        elif a[-2]+a[-1]=='ic':
            print('Godo')
        elif a[-2]+a[-1]=='as':
            print('Griego')
        elif a[-2]+a[-1]=='af':
            print('Normando')
        elif a[-2]+a[-1]=='is' or a[-2]+a[-1]=='ax' :
            print('Breton')
        elif a[-2]+a[-1]=='ez':
            print('Hispano')
        elif a[-1]=='a':
            print('Indio')
        else:
            print('Desconocido')
            
