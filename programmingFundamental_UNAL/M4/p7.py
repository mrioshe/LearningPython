X=input()
Y=input()
if X==Y:
    print('empate')
elif (X=='piedra' and Y=='papel') or (X=='papel' and Y=='piedra') :
    print('papel vence piedra')
elif (X=='piedra' and Y=='tijera') or (X=='tijera' and Y=='piedra') :
    print('piedra vence tijera')
elif (X=='papel' and Y=='tijera') or (X=='tijera' and Y=='papel') :
    print('tijera vence papel')
