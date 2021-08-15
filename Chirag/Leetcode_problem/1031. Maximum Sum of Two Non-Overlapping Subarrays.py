def maxSumTwoNoOverlap(nums,x, y):
    n=len(nums)
    dp1=[0]*n
    dp2=[0]*n
    cursum=0
    for i in range(n):
        if i < x:
            cursum+=nums[i]
            dp1[i]=cursum
        else:
            cursum+=nums[i]-nums[i-x]
            dp1[i]=max(dp1[i-1],cursum)
    cursum=0
    for i in range(n-1,-1,-1):
        if i+y>=n:
            cursum+=nums[i]
            dp2[i]=cursum
        else:
            cursum+=nums[i]-nums[i+y]
            dp2[i]=max(dp2[i+1],cursum)
    ans=0
    for i in range(x-1,n-y):
        
        ans=max(ans,dp1[i]+dp2[i+1])
    
    dp1=[0]*n
    dp2=[0]*n
    cursum=0
    for i in range(n):
        if i < y:
            cursum+=nums[i]
            dp1[i]=cursum
        else:
            cursum+=nums[i]-nums[i-y]
            dp1[i]=max(dp1[i-1],cursum)
    cursum=0
    for i in range(n-1,-1,-1):
        if i+x>=n:
            cursum+=nums[i]
            dp2[i]=cursum
        else:
            cursum+=nums[i]-nums[i+x]
            dp2[i]=max(dp2[i+1],cursum)
    for i in range(y-1,n-x):
        ans=max(ans,dp1[i]+dp2[i+1])
    return ans
#faster approach
def maxSumTwoNoOverlap1(A, L, M):
    if len(A) < L + M: return 0
    for i in range(1, len(A)):
        A[i] += A[i - 1]
    res, maxL, maxM = A[L + M - 1], A[L - 1], A[M - 1]
    #print(M,L,maxL,maxM,res)
    for i in range(L + M, len(A)):
        #print(i,maxL,maxM,res)
        maxL = max(maxL, A[i - M] - A[i - M - L])
        #print(maxL,A[i-M],A[i-M-L])
        maxM = max(maxM, A[i - L] - A[i - L - M])
        #print(maxM,A[i-L],A[i-L-M])
        res = max(res, maxL + A[i] - A[i - M], maxM + A[i] - A[i - L])
        #print(res,A[i],A[i-M],A[i-L])
    return res
print(maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4],1,2))
print(maxSumTwoNoOverlap1([0,6,5,2,2,5,1,9,4],1,2))           
        
