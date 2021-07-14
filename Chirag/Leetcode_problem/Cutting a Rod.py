def recur(A,S,W):
    if S==0 or W==0:
        return 0
    if S>W:
        return recur(A,S-1,W)
    else:
        return max(recur(A,S-1,W),A[S-1]+recur(A,S,W-S))

def tab(A,S,W,dp):
    if S==0 or W==0:
        return 0
    if dp[S][W]!=-1:
        return dp[S][W]
    if S>W:
        dp[S][W]= tab(A,S-1,W,dp)
    else:
        dp[S][W]=max(tab(A,S-1,W,dp),A[S-1]+tab(A,S,W-S,dp))
    return dp[S][W]
    
def printmat(dp):
    for row in dp:
        print(row)
    
    

if __name__=='__main__':
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    size = len(arr)
    W=12
    dp=[[-1 for _ in range(W+1)]for _ in range(size+1)]
    print(tab(arr,size,W,dp))
    printmat(dp)
