def mem(price,weight,W,n):
    if n==0 or W==0:
        return 0
    if dp[n][W]!=-1:
        return dp[n][W]
    if weight[n-1]>W:
        dp[n][W]= mem(price,weight,W,n-1)
        return dp[n][W]
    else:
        dp[n][W]= max(mem(price,weight,W,n-1),price[n-1]+mem(price,weight,W-weight[n-1],n-1))
        return dp[n][W]

def tab(price,weight,W,n):
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif weight[i-1]>W:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],price[i-1]+dp[i-1][j-weight[i-1]])
    return dp[n][W]
    
def printmat(dp):
    for i in dp:
        print(i)
    print('======================')
if __name__=='__main__':
    price=[10,15,20]
    weight=[1,2,3]
    W=6
    n=len(price)
    dp=[[-1 for _ in range(W+1)] for __ in range(n+1)]
    #print(mem(price,weight,W,n))
    print(tab(price,weight,W,n))
    printmat(dp)
    




    
