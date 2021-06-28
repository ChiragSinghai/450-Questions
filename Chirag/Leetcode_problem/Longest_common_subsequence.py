def printmat(dp):
    for row in dp:
        print(row)
    print('==================')
def LCS(str1,str2):
    m=len(str1)
    n=len(str2)
    dp=[[0 for _ in range(n+1)]for _ in range(m+1)]
    printmat(dp)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    printmat(dp)
    print(dp[m][n])
    printLCS(dp,str1)

def printLCS(dp,str1):
    m=len(dp)-1
    n=len(dp[0])-1
    print(m)
    s=''
    #index=dp[m][n]-1
    while m!=0 and n!=0:
        #print(m,n)
        upValue=dp[m-1][n]
        leftValue=dp[m][n-1]
        diValue=dp[m-1][n-1]
        if upValue==leftValue==diValue and dp[m][n]!=diValue:
            m-=1
            n-=1
            s+=str1[m]
            
        elif leftValue<upValue:
            m-=1
        else:
            n-=1
    print(s[::-1])

if __name__=='__main__':
    s1="GXTXAYB"
    s2="AGGTAB"
    LCS(s1,s2)
