a = int(input())
b = int (input())
c = input()
if c == 'am' and a==12:
    print ('Faltan',23*60+60-b ,'para las 12')
elif c == 'pm' and a==12:
    print ('Faltan',11*60+60-b ,'para las 12')
elif c == 'am' and a!=12:
    print('Faltan',12*60+(11-a)*60+60-b ,'para las 12')
else:
    print ('Faltan',(11-a)*60+60-b ,'para las 12')
