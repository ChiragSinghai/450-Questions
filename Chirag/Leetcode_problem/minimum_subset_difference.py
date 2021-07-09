def printmat(dp):
    for row in dp:
        print(row)
        
def findmin(A,n,S):
    dp=[[False for i in range(S+1)]for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
        
    for i in range(1,n+1):
        for j in range(1,S+1):
            if j < A[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-A[i-1]]
    printmat(dp)
    
    
    

if __name__=='__main__':
    A=[4,1,1,5]
    n=len(A)
    S=sum(A)
    findmin(A,n,S)
