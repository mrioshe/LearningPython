C = int(input())
K = int(input())
if (K-C)> 0:
    print('Hubo una ganancia de $',K-C, 'correspondiente al',(K-C)*100/C,'% del capital invertido')
elif (K-C)<0:
    print('Hubo una perdida de $',abs(K-C), 'correspondiente al',abs((K-C)*100/C),'% del capital invertido')
else:
    print('No hubo ni ganancia ni perdida, la inversion fue un desperdicio de tiempo, pero al menos no de dinero')
