def getcandies(A):
    n=len(A)
    C=[1]*n
    for i in range(1,n):
        if A[i-1]<A[i]:
            C[i]=C[i-1]+1
    print(C)
    for i in range(n-2,-1,-1):
        if A[i]>A[i+1]:
            C[i]=max(C[i],C[i+1]+1)
    print(C)
    print(sum(C))
        
if __name__=='__main__':
    A=[1,3,4,5,2]
    getcandies(A)
