def minOperations(nums):
    n=len(nums)
    
    change=0
    for i in range(1,n):
        if nums[i]<=nums[i-1]:
            change+=nums[i-1]-nums[i]+1
            nums[i]+=nums[i-1]-nums[i]+1
    return change
    
