X= float(input())
Y=float(input())
if X==0 and Y==0:
    print('La coordenada (',X,', ',Y,') corresponde al origen', sep='')
elif X==0:
    print('La coordenada (',X,', ',Y,') esta sobre el eje Y', sep = '')
elif Y==0:
    print('La coordenada (',X,', ',Y,') esta sobre el eje X', sep = '')
elif Y>0 and X>0:
    print('La coordenada (',X,', ',Y,') se encuentra en el cuadrante 1', sep = '')
elif Y>0 and X<0:
    print('La coordenada (',X,', ',Y,') se encuentra en el cuadrante 2', sep = '')
elif Y<0 and X<0:
    print('La coordenada (',X,', ',Y,') se encuentra en el cuadrante 3', sep = '')
else:
    print('La coordenada (',X,', ',Y,') se encuentra en el cuadrante 4', sep = '')
    
