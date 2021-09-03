def threeSum(nums):
    
    if len(nums) < 3:
        return []
    nums.sort()
    
    ans = []
    
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = len(nums) - 1
        
        target = -nums[i]
        
        while left < right:
            if nums[left] + nums[right] == target:
                ans.append([nums[i], nums[left], nums[right]])
                left+=1
                right-=1
                
                while left < right and nums[left] == nums[left-1]:
                    # same val seen for 2 sum
                    left+=1
                
                while right > left and nums[right] == nums[right+1]:
                    right-=1
            else:
                if nums[left] + nums[right] > target:
                    # too large
                    right-=1
                    
                    while right > left and nums[right] == nums[right+1]:
                        right-=1
                else:
                    left+=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
    return ans
#faster approach
def threeSum1(nums):
    nums.sort()
    res=[]
    n=len(nums)
    for i,e in enumerate(nums):
        if i>0 and e==nums[i-1]:
            continue
        l=i+1
        r=n-1
        while l<r:
            if e+nums[l]+nums[r]<0:
                l+=1
            elif e+nums[l]+nums[r]>0:
                r-=1
            else:
                res.append([e,nums[l],nums[r]])
                l+=1
                while nums[l]==nums[l-1] and l<r:
                    l+=1
    return res
print(threeSum1([-1,0,1,-1]))
