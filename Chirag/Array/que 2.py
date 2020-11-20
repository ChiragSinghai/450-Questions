def find(a):
    mi=ma=a[0]
    for i in range(1,len(a)):
        if a[i]<mi:
            mi=a[i]
        else:
            if a[i]>ma:
                ma=a[i]
    print('Minimum:',mi)
    print('Maximum:',ma)

if __name__=='__main__':
    arr=list(map(int,input().split()))
    find(arr)
    print('min:',min(arr)+'\nmax:',max(arr))
