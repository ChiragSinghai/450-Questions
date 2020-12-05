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

def anotherapproach(A,n,k):
    A.sort()
    count=1
    m=n//k
    i=1
    check=True
    while i<n:
        if A[i]==A[i-1]:
            count+=1
            if count>=m and check:
                check=False
                print(A[i])
        else:
            check=True
            count=1
        i+=1
        
if __name__=='__main__':
    fun([1,2,2,2,3,3,4,4,4,4],8,4)
    anotherapproach([1,2,2,3,4,4,4,4],8,4)

        
