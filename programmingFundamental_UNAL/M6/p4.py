l=[]
while True:
    l.append(int(input()))
    if l[-1]==0:
        l.pop(-1)
        break
l.sort()
print((l[-3]-l[2])/(len(l))**2)

