tarifa= int(input())
horas= int(input())
if horas > 45:
    print('$', int(horas*tarifa+(horas-45)*tarifa*50/100))
else:
    print('$', horas*tarifa)
