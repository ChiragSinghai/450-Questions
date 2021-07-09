def printmat(dp):
    for row in dp:
        print(row)
        
def findmin(A,n,S):
    dp=[[False for i in range(S+1)]for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    printmat(dp)
    
    

if __name__=='__main__':
    A=[4,3,1,7]
    n=len(A)
    S=4
    findmin(A,n,S)
