def findamount(A):
    n=len(A)
    if not n:
        return 0
    if n==1:
        return A[0]
    if n==2:
        return max(A[0],A[1])
    dp=[0]*n
    dp[0]=A[0]
    dp[1]=max(A[0],A[1])
    for i in range(2,n):
        dp[i]=max(A[i]+dp[i-2],dp[i-1])
    return dp[n-1]

def findamount2(A):
    n=len(A)
    if not n:
        return 0
    if n==1:
        return A[0]
    if n==2:
        return max(A[0],A[1])
    m1=A[0]
    m2=max(A[1],A[0])
    for i in A[2:]:
        temp=max(i+m1,m2)
        m1=m2
        m2=temp
    return m2
    

if __name__=='__main__':
    A=[5, 3, 4, 11, 2]
    #A=[6, 7, 1, 3, 8, 2, 4]
    print(findamount(A))
    print(findamount2(A))
    
