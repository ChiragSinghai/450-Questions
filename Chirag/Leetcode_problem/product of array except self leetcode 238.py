def productExceptSelf(nums) :
    total_product = 1
    A=[0]*len(nums)
    count=nums.count(0)
    if count>=2:
        
        return A
    else:
        for i in nums:
            if i != 0:
                total_product*=i
        if count == 1:
            
            A[nums.index(0)]=total_product
        else:
            for i in range(len(nums)):
                A[i]=total_product//nums[i]
    return A
print(productExceptSelf([1,2,3,4]))
        
