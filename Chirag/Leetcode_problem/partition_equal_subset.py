def recur(A,n,S):
    if S==0:
        return True
    if n==0 :
        return False
    if A[n-1]>S:
        return recur(A,n-1,S)
    else:
        return recur(A,n-1,S)or recur(A,n-1,S-A[n-1])

def tab(A,n,S,dp):
    if S==0:
        return True
    if n==0:
        return False
    if dp[n][S]!=-1:
        return dp[n][S]
    if A[n-1]<=S:
        dp[n][S]=tab(A,n-1,S,dp) or tab(A,n-1,S-A[n-1],dp)
    else:
        dp[n][S]=tab(A,n-1,S,dp)
    return dp[n][S]
def printmat(dp):
    for row in dp:
        print(row)
    print('=========================')
def mem(A,n,S):
    dp=[[-1 for i in range(S+1)]for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for j in range(1,S+1):
        dp[0][j]=False
    #printmat(dp)
    for i in range(1,n+1):
        for j in range(1,S+1):
            if j<A[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-A[i-1]]
    printmat(dp)
    print(dp[n][S])
if __name__=='__main__':
    A=[1,5,6,3,3]
    n=len(A)
    S=sum(A)
    if S & 1:
        print('False')
    else:
        S=S//2
        dp=[[-1 for i in range(S+1)]for i in range(n+1)]
        print(tab(A,n,S,dp))

