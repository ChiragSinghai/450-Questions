def minimumDeleteSum(s1, s2):
    total = 0
    for c in s1:
        total += ord(c)
    for c in s2:
        total += ord(c)
    n = len(s1) + 1 
    m = len(s2) + 1
            # +1 is a trick to avoid out of bounds exceptions
    dp = [[0 for i in range(n)] for j in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = ord(s1[j-1]) + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    for row in dp:
        print(row)
    return total - 2 * dp[-1][-1]
def minimumDeleteSum1(s1, s2):
    m=len(s1)
    n=len(s2)
    dp=[[0 for _ in range(n+1)]for _ in range(m+1)]
    for i in range(m-1,-1,-1):
        dp[i][n]=dp[i+1][n]+ord(s1[i])
    for j in range(n-1,-1,-1):
        dp[m][j]=dp[m][j+1]+ord(s2[j])
    for row in dp:
        print(row)
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if s1[i]==s2[j]:
                dp[i][j]=dp[i+1][j+1]
            else:
                dp[i][j]=min(dp[i+1][j]+ord(s1[i]),dp[i][j+1]+ord(s2[j]))
    return dp[0][0]


print(minimumDeleteSum("delete","leet"))
print([ord(i) for i in 'delete'])
        
