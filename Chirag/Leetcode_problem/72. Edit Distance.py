def minDistance( word1, word2):
    m=len(word1)
    n=len(word2)
    dp=[[float("inf")]*(n+1) for _ in range(m+1)]
    for row in dp:
        print(row)
    for i in range(n+1):
        dp[m][i]=n-i
    for i in range(m+1):
        dp[i][n]=m-i
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if word1[i]==word2[j]:
                dp[i][j]=dp[i+1][j+1]
            else:
                dp[i][j]=1+min(dp[i+1][j],dp[i+1][j+1],dp[i][j+1])
            print(dp[i][j],word1[i],word2[j])
    print('=====================')
    for row in dp:
        print(row)
    return dp[0][0]
print(minDistance('horse','ros'))
