#brute force
def isMatch(s, p) :
        
    def dfs(i,j):
        if i>=len(s) and j>=len(p):
            return True
        if j>=len(p):
            return False
        match = i<len(s) and (s[i]==p[j] or p[j]=='.')
        if j+1<len(p) and p[j+1]=='*':
            return (dfs(i,j+2) or (match and dfs(i+1,j)))
        if match:
            return dfs(i+1,j+1)
        return False
    return dfs(0,0)

# top down memorization
def isMatch1( s, p) :
    dp=[[-1 for _ in range(len(p)+1)]for _ in range(len(s)+1)]
    def dfs(i,j):
        if dp[i][j]!=-1:
            return dp[i][j]
        if i>=len(s) and j>=len(p):
            return True
        if j>=len(p):
            return False
        
        match = i<len(s) and (s[i]==p[j] or p[j]=='.')
        if j+1<len(p) and p[j+1]=='*':
            dp[i][j]=(dfs(i,j+2) or (match and dfs(i+1,j)))
            return dp[i][j]
        if match:
            dp[i][j]=dfs(i+1,j+1)
            return dp[i][j]
        dp[i][j]=False
        return dp[i][j]
    
    return dfs(0,0) 
def printmat(dp):
    for row in dp:
        print(row)
def isMatch2(s, p):
        dp=[[False for _ in range(len(p)+1)]for _ in range(len(s)+1)]
        dp[-1][-1]=True
        printmat(dp)
        for i in range(len(s),-1,-1):
            for j in range(len(p)-1,-1,-1):
                match= i<len(s) and (s[i]==p[j] or p[j]=='.')
                if j+1<len(p) and p[j+1]=='*':
                    dp[i][j]=dp[i][j+2] or (match and dp[i+1][j])
                else:
                    dp[i][j]=match and dp[i+1][j+1]
        return dp[0][0]
                    
a="aab"
b="c*a*b"
print(isMatch2(a,b))


