def zeller(d,m,y):
    if m==14 or m==13:
        y+=-1
    dia=(d+(13*(m+1))//5 + y + y//4 - y//100 + y//400) % 7
    return(dia)

dic_mes={'enero':13,'febrero':14,'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':
     8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12}
dic_days={'0':'sabado','1':'domingo','2':'lunes','3':'martes','4':'miercoles','5':'jueves',
          '6':'viernes'}

N=int(input())
if N <=1000:
    for i in range(N):
        fecha=input().split('-')
        print(dic_days[str(zeller(int(fecha[0]),dic_mes[fecha[1]],int(fecha[2])))])
