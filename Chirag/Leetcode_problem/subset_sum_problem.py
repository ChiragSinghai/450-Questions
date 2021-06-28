def tab(A,S,n):
    if n==0:
        dp[n][S]= False
    if S==0:
        dp[n][S] =True
    if dp[n][S]!=-1:
        return dp[n][S]
    if A[n-1]>S:
        dp[n][S]= tab(A,S,n-1)
    else:
        dp[n][S]= tab(A,S,n-1) or tab(A,S-A[n-1],n-1)
    return dp[n][S]
def printmat(dp):
    for row in dp:
        print(row)
    print('======================')
def mem(A,S,n):
    dp=[[-1 for _ in range(S+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for j in range(1,S+1):
        dp[0][j]=False
    #printmat(dp)
    for i in range(1,n+1):
        for j in range(1,S+1):
            if j<A[i-1]:
                dp[i][j]= dp[i-1][j]
            if j>=A[i-1]:
                dp[i][j]= dp[i-1][j] or dp[i-1][j-A[i-1]]
    printmat(dp)
    return dp[n][S]
            
if __name__=='__main__':
    A=[3, 34, 4, 12, 1,5, 2]
    S=9
    n=len(A)
    dp=[[-1 for _ in range(S+1)] for _ in range(n+1)]
    #printmat(dp)
    print(mem(A,S,n))
    #printmat(dp)
