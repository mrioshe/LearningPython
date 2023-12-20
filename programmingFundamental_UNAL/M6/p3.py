l=[]
while True:
    l.append(input())
    if l[-1]=='0':
        break
print(len(list(set(l)))-1)
