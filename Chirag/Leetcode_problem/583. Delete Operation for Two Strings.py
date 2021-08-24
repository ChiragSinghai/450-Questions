def minDistance(word1, word2):
    def LCS(s1,s2,m,n):
        dp=[[0 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        #print(dp)
        return dp[m][n]
    m=len(word1)
    n=len(word2)
    l=LCS(word1,word2,m,n)
    #print(l)
    return (m+n)-(2*l)
print(minDistance('SEAM','EATM'))
