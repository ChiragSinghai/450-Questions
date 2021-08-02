def rec(W,b,e,y):
    if dp[b][e]!=-1:
        return dp[b][e]
    if b==e:
        return W[b]*y

    x = W[b]*y + rec(W,b+1,e,y+1)
    z = W[e]*y + rec(W,b,e-1,y+1)
    dp[b][e]=max(x,z)
    return dp[b][e]

def printmat(dp):
    for row in dp:
        print(row)
    print('====================')
W = [ 2, 4, 6, 2, 5 ]
cur_year = 1
n=len(W)
dp=[[-1 for _ in range(n)]for _ in range(n)]
print(rec(W,0,n-1,cur_year))
printmat(dp)
