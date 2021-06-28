def printmatrix(mat):
    for row in mat:
        print(row)
    print("=============")
        
def maxways(coins,amount):
    n=len(coins) 
    dp=[[0 for i in range(amount+1)]for i in range(n)]
    for i in range(n):
        dp[i][0]=1
    for i in range(n):
        for j in range(1,amount+1):
            x=dp[i-1][j] if i>0 else 0
            y=dp[i][j-coins[i]] if j-coins[i]>=0 else 0
            dp[i][j]=x+y
            
    printmatrix(dp)
    return dp[n-1][amount]
def maxways2(coins,amount):
    n=len(coins)
    dp=[[0 for i in range(n)]for i in range(amount+1)]
    for i in range(n):
        dp[0][i]=1
    for i in range(1,amount+1):
        for j in range(n):
            x=dp[i][j-1] if j>0 else 0
            y=dp[i-coins[j]][j] if i-coins[j]>=0 else 0
            dp[i][j]=x+y

    printmatrix(dp)
    return dp[amount][n-1]
if __name__=='__main__':
    coins=[2,3,5,10]
    amount=15
    print(maxways2(coins,amount))
    print(maxways(coins,amount))
    
