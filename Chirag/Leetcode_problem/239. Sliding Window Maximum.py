import collections
def maxSlidingWindow(nums, k) :
    if k ==1:
        return nums
    result=[]
    queue=collections.deque()
    for i in range(k):
        while queue and queue[-1]<nums[i]:
            queue.pop()
        queue.append(nums[i])
    result.append(queue[0])
    for i in range(k,len(nums)):
        if nums[i-k]>=queue[0]:
            queue.popleft()
        while queue and queue[-1]<nums[i]:
            queue.pop()
        queue.append(nums[i])
        result.append(queue[0])
    return result
A=[1,3,5,6,7,8]
print(maxSlidingWindow(A,2))
