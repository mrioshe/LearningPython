a=open('mensaje.txt','r')
for renglon in a:
    s=''
    b=renglon.replace('\n','')
    for i in range(len(b)):
        s+=b[-i-1]
    print(s)      
a.close()
