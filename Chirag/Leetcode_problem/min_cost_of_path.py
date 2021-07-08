#we have to find the min cost of a 2d array  starting from
# upperleft index to the bottom right element

def printmat(dp):
    for row in dp:
        print(row)
def findMinCost(A,m,n):
    dp=[[0 for i in range(n)] for i in range(m)]
    for i in range(m):
        if i:
            dp[i][0]=dp[i-1][0]+A[i][0]
        else:
            dp[i][0]=A[i][0]
    for i in range(n):
        if i:
            dp[0][i]=dp[0][i-1]+A[0][i]
        else:
            dp[0][i]=A[0][i]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=min(dp[i-1][j],dp[i][j-1])
            dp[i][j]+=A[i][j]
    printmat(dp)


        
    
if __name__=='__main__':
    A=[[3,4,5,6],
       [4,5,2,1],
       [2,1,5,7],
       [1,4,2,7]]
    m=len(A)
    n=len(A[0])
    findMinCost(A,m,n)
