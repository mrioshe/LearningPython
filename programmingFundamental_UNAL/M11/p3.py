from random import randint
c=int(input())
for i in range(c):
    plataforma_ven_a_mi=int(input())
    suma=randint(1,6)+randint(1,6)
    if suma>plataforma_ven_a_mi:
        print('Gana el humano')
    elif suma==plataforma_ven_a_mi:
        print('Empate')
    else:
        print('Gana la plataforma')
        
