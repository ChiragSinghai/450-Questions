def tab(A,n,S):
    print('here')
    if S==0:
        return 1
    if n==0:
        return 0
    if dp[n][S]!=-1:
        return dp[n][S]
    if S<A[n-1]:
        dp[n][S]=tab(A,n-1,S)
    else:
        dp[n][S]=tab(A,n-1,S)+tab(A,n-1,S-A[n-1])
    return dp[n][S]

def printmat(dp):
    for row in dp:
        print(row)

def mem(A,n,S):
    dp=[[-1 for i in range(S+1)]for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    for j in range(1,S+1):
        dp[0][j]=0
    for i in range(1,n+1):
        for j in range(1,S+1):
            if j < A[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-A[i-1]]
    return dp[n][S]
if __name__=='__main__':
    A=[1,5,6,3,3]
    n=len(A)
    S=sum(A)
    if S & 1:
        print('False')
    else:
        S=S//2
        dp=[[-1 for _ in range(S+1)] for _ in range(n+1)]
        print(tab(A,n,S))
        printmat(dp)
