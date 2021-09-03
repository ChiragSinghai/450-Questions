def maxProfit(prices):
    n=len(prices)
    dp1=[0]*n
    dp2=[0]*n
    lsf=prices[0]
    for i in range(1,n):
        if prices[i]<lsf:
            lsf=prices[i]
        pist=prices[i]-lsf  #pist: price if sold today
        if pist>dp1[i-1]:
            dp1[i]=pist
        else:
            dp1[i]=dp1[i-1]
    msf=prices[-1]
    for i in range(n-2,-1,-1):
        if prices[i]>msf:
            msf=prices[i]
        pibt=msf-prices[i] #pibt:price if bought today
        if pibt>dp2[i+1]:
            dp2[i]=pibt
        else:
            dp2[i]=dp2[i+1]
    msf=0 #max so far
    for i in range(n):
        if dp1[i]+dp2[i]>msf:
            msf=dp1[i]+dp2[i]
    return msf    
print(maxProfit([1,2,3,7,6,4,8,2]))        
