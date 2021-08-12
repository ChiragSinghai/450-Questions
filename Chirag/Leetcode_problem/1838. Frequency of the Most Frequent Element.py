def maxFrequency(nums, k):
    nums.sort()
    total=0
    res=0
    l=0
    r=0
    while r<len(nums):
        total+=nums[r]
        while nums[r]*(r-l+1)>total+k:
            total-=nums[l]
            l+=1
        res=max(res,r-l+1)
        r+=1
    return res
print(maxFrequency([1,1,2,1,4,2],2))

