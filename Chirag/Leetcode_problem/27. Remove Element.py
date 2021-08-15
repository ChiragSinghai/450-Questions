def removeElement(nums, val):
    if not nums:
        return 0
    right=len(nums)-1
    left=0
    
    while right>=0 and nums[right]==val:
        right-=1
    while left<right:
        if nums[left]==val:
            nums[left],nums[right]=nums[right],nums[left]
            right-=1
            while right>=0 and nums[right]==val:
                right-=1
        left+=1
        
    return right+1
A=[1,3,4,2,5,7,2,8,2,3,2]
print(A[:removeElement(A,2)])
