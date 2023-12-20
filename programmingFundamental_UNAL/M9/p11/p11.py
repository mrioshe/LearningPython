a=open('trifelios.txt','r')
for renglon in a:
    b=renglon.replace('\n','').split('-')
    c=False
    for i in range(len(b[0])):
        if b[0][i:]+b[0][0:i] == b[1]:
            c=True
            break
    if c:
        print('Es trifelio')
    else:
        print('No es trifelio')
a.close()    
