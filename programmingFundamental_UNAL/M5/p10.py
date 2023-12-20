l=int(input())
h=int(input())
for i in range(1,h+1):
    if i== (h-1)/2 + 1:
        print('+'*l)
    else:
        print('0'*int((l-1)/2)+'+'+'0'*int((l-1)/2))
