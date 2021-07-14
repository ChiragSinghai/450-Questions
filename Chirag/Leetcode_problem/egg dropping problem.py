INT_MAX = 32767
def findmintry(ne,nf):
    dp=[[0 for _ in range(ne+1)]for _ in range(nf+1)]
    
    for i in range(1,ne+1):
        dp[1][i]=1
        dp[0][i]=0
    for i in range(0,nf+1):
        dp[i][1]=i
    printmat(dp)
    for i in range(2,nf+1):
        for j in range(2,ne+1):
            dp[i][j]=INT_MAX
            for k in range(1,i+1):
                c=1+max(dp[k-1][j-1],dp[i-k][j])
                if c<dp[i][j]:
                    dp[i][j]=c
    printmat(dp)
    
def printmat(dp):
    for row in dp:
        print(row)
    print('==========================')


    

if __name__=='__main__':
    n_eggs=5
    n_floor=10
    findmintry(n_eggs,n_floor)
