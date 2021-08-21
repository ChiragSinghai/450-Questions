def subarraySum(nums,k):
        D={}
        D[0]=1
        res=0
        cursum=0
        for i in nums:
            cursum+=i
            diff=cursum-k
            res += D.get(diff,0)
            D[cursum]=1+D.get(cursum,0)
        return res
print(subarraySum([1,1,1],2))
print(subarraySum([1,2,3],3))
