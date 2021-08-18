def searchRange(nums,target):
    if not nums:
        return [-1,-1]
    l=0
    r=len(nums)-1
    if r==0 and nums[0]==target:
        return [0,0]
    def binary(l,r):
        if l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return binary(l,mid-1)
            else:
                return binary(mid+1,r)
        else:
            return -1
    mid=binary(l,r)
    
    if mid==-1:
        return [-1,-1]
    l=mid
    while l>0 and  nums[l-1]==target:
        l-=1
    
    while mid<r and nums[mid+1]==target:
        mid+=1
    return [l,mid]


print(searchRange([1,1],1))
