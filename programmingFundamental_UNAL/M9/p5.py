N=int(input())
if N <=500:
    for i in range(N):
        a=input()
        if 'a' in a and 'e' in a and 'i' in a and 'o' in a and 'u' in a:
            print('Panvocalica')
        else:
            print('No es panvocalica')
