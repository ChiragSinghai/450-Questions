def getJumps(A):
    dp=[float('inf') for _ in A]
    dp[0]=0
    for i in range(len(A)):
        j=i+1
        while j<=i+A[i] and j<len(A):
            dp[j]=min(1+dp[i],dp[j])
            j+=1
    return dp[-1]




B=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
A=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(getJumps(B))
