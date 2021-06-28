def recur(A,S,n):
    if S==0:
        return 1
    if n==0:
        return 0
    if A[n-1]>S:
        return recur(A,S,n-1)
    else:
        return recur(A,S,n-1)+recur(A,S-A[n-1],n-1)

def tab(A,S,n):
    if n==0:
        dp[n][S]=0
    if S==0:
        dp[n][S]=1
    if dp[n][S]!=-1:
        return dp[n][S]
    if A[n-1]>S:
        dp[n][S]=tab(A,S,n-1)
    else:
        dp[n][S]=tab(A,S,n-1)+tab(A,S-A[n-1],n-1)
    return dp[n][S]

def printmat(dp):
    for row in dp:
        print(row)
    print('========================')
def mem(A,S,n):
    dp=[[-1 for _ in range(S+1)] for _ in range(n+1)]
    mask=1<<n
    print(bin(mask-1))
    for j in range(S+1):
        dp[0][j]=0
    for i in range(n+1):
        dp[i][0]=1
    
    
    for i in range(1,n+1):
        for j in range(1,S+1):
            if A[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-A[i-1]]
    printmat(dp)
    subset(dp,n,S,A)
    return dp[n][S]
def subset(dp,n,S,A):
    queue=[(n,S,[])]
    counter=10
    while queue:
        #print(queue)
        i,j,L=queue.pop(0)
        #print(i,j,id(L))
        
        if i==0 and j==0:
            print((L))
            continue
        exc=dp[i-1][j]
        #print(inc)
        if exc:
            B=list(L)
            queue.append((i-1,j,B.copy()))
        
        if (j>=A[i-1]):
            inc=dp[i-1][j-A[i-1]]
            if inc:
                B=list(L+[A[i-1]])
                queue.append((i-1,j-A[i-1],B.copy()))
        counter-=1
    
if __name__=='__main__':
    A=[3, 34, 4, 12, 1,5,2]
    S=9
    n=len(A)

    dp=[[-1 for _ in range(S+1)] for _ in range(n+1)]
    print(mem(A,S,n))
