def get1(n):
    offset=1
    dp=[0]*n
    for i in range(1,n):
        if offset*2==i:
            offset=i
        dp[i]=1+dp[i-offset]
        print('hey')
    print(dp)
if __name__=='__main__':
    n=10
    get1(n+1)
#printing the no. of 1 in the number
#ex: n=5
#return array =[0,1,1,2,1,2]
#array show the number of 1 in the indexes

