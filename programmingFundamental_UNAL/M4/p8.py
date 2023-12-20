k=int(input())

if k>=50000:
    cincuenta=k//50000
    veinte=k%50000//20000
    diez=k%50000%20000//10000
    cinco=k%50000%20000%10000//5000
    dos=k%50000%20000%10000%5000//2000
    uno=k%50000%20000%10000%5000%2000//1000
elif k>=20000:
    cincuenta = 0
    veinte=k//20000
    diez=k%20000//10000
    cinco=k%20000%10000//5000
    dos=k%20000%10000%5000//2000
    uno=k%20000%10000%5000%2000//1000
elif k>=10000:
    cincuenta = 0
    veinte=0
    diez=1
    cinco=k%10000//5000
    dos=k%10000%5000//2000
    uno=k%10000%5000%2000//1000
elif k>5000:
    cincuenta = 0
    veinte=0
    diez=0
    cinco=1
    dos=k%5000//2000
    uno=k%5000%2000//1000
elif k>2000:
    cincuenta = 0
    veinte=0
    diez=0
    cinco=0
    dos=k//2000
    uno=k%2000//1000
elif k>2000:
    cincuenta = 0
    veinte=0
    diez=0
    cinco=0
    dos=0
    uno=k//1000
else:
    cincuenta = 0
    veinte=0
    diez=0
    cinco=0
    dos=0
    uno=1
if cincuenta !=0:
    print(cincuenta, 'de $50000')
if veinte !=0:
    print(veinte,'de $20000')
if diez !=0:
    print(diez,'de $10000')
if cinco !=0:
    print(cinco,'de $5000')
if dos !=0:
    print(dos,'de $2000')
if uno !=0:
    print(uno,'de $1000')
    
        
