def thirdMax(nums):

    nums=list(set(nums))
    n=len(nums)
    if n<=2:
        return max(nums)
    
    for i in range(3):
        curr=0
        for j in range(n-i):
            if nums[curr]<nums[j]:
                curr=j
        nums[curr],nums[len(nums)-1-i]=nums[len(nums)-1-i],nums[curr]
        #print(nums)
    return nums[-3]
print(thirdMax([1,2,5,6,7]))
