def fun(A,n,k):
    d={}
    for i in A:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    m=n/k
    for i in d:
        if d[i]>=m:
            print(i)

        
