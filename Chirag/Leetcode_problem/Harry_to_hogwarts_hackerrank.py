n=input()
L=list(n)
step=0
if int(n)==6174:
    print(step)
else:
    while True:
        step+=1
        L.sort()
        asc=int(''.join(L))
        dsc=int(''.join(L[::-1]))
        n=dsc-asc
        if n==6174:
            print(step)
            break
        L=list(str(n))
