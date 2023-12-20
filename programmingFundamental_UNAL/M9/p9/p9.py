a=open('cadena.txt','r')
for renglon in a:
    b=renglon.split()
    c=0
    for i in range(len(b)-1):
        
        if b[i][len(b[i])-2:len(b[i])]==b[i+1][0:2] or b[i][len(b[i])-3:len(b[i])]==b[i+1][0:3]:
            c += 1
    if c==len(b)-1:
        print('cadena completa')
    else:
        print('cadena rota')
            
