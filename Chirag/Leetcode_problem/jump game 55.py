def solution(nums):
    goal= len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if i+nums[i]>= goal:
            goal=i
    return True if goal==0 else False
def solution2(nums):
    reach = 0
    n=len(nums)
    for i in range(n):
        if reach<i:
            return False
        reach = max(reach,nums[i]+i)
            
    return True
A=[5,9,3,2,1,0,2,3,3,1,0,0]
print(solution2(A))
