import sys
A=[1,3,5,7]
T=8
def printmat(dp):
    for row in dp:
        print(row)
    print('=========================')
def mincoin(coins,amt,i):
    if amt==0:
        return 0
    if i>len(coins)-1 or amt<0:
        return sys.maxsize
    #m=sys.maxsize
    result=min(1+mincoin(coins,amt-coins[i],i),mincoin(coins,amt,i+1))
    return result
#optimal DP solution bottomup approach
def mincoin1(coins,amt):
    dp=[[0 for i in range(amt+1)]for i in range(len(coins)+1)]
    printmat(dp)
    for i in range(1,amt+1):
        dp[0][i]=5000
    for i in range(1,len(coins)+1):
        for j in range(1,amt+1):
            if j < coins[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                include=1+dp[i][j-coins[i-1]]
                exclude=dp[i-1][j]
                dp[i][j]=min(include,exclude)
                
    printmat(dp)
    return dp[len(coins)][amt]
# DP solution top down approach
dp=[[-1 for i in range(T+1)]for i in range(len(A))]
#for i in range(1,T):
 #   dp[0][i]=500

def mincoin3(dp,A,T,i):
    if T==0:
        return 0
    if T<0 or i < 0:
        #dp[i][T]=500
        return 500
    
    if dp[i][T]!=-1:
        return dp[i][T]
    #exclude condition
    exclude=mincoin3(dp,A,T,i-1)
    include=1+mincoin3(dp,A,T-A[i],i)
    print(i,T)
    dp[i][T]=min(exclude,include)
    return dp[i][T]
mincoin3(dp,A,T,len(A)-1)
printmat(dp)
#print(mincoin1(A,T)) 
    
