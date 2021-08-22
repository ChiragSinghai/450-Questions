def lengthOfLIS(nums):
    n=len(nums)
    dp=[1 for _ in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if nums[i]<nums[j]:
                dp[i]=max(dp[i],1+dp[j])
            
    return max(dp)

def lengthOfLIS1(nums):
    array = [1]*len(nums)
    
    for i in range(len(nums)):
        curr = 0
        for j in range(i-1,-1,-1):
            if nums[j] < nums[i] and array[j] >= curr :
                curr = array[j]
        array[i] += curr
    return max(array)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))


