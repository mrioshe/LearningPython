a=open('conversaciones.txt','r')
opositivos=['Sin embargo','No obstante','Ahora bien','Aun asi']
causativos=['Por tanto','Dado que','Por consiguiente','Asi pues','Por ende']
for renglon in a:
    c1=0
    c2=0
    for i in range(len(opositivos)):
        if opositivos[i].lower() in renglon.lower():
            c1 +=1
    for k in range(len(causativos)):
        if causativos[k].lower()  in renglon.lower():
            c2 +=1
    print('Opositivos',c1,'Causativos',c2)

a.close()

    
