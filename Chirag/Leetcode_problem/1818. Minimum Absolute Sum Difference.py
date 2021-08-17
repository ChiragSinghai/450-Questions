import bisect
def minAbsoluteSumDiff(nums1, nums2) -> int:
    modulo=(10**9+7)
    store=nums1.copy()
    store=sorted(store)
    n=len(nums1)
    max_diff=0
    res=0
    for i in range(n):
        res+=abs(nums1[i]-nums2[i])
        if nums1[i]!=nums2[i]:
            index=bisect.bisect_left(store,nums2[i])
            left=store[index-1] if index>0 else store[0]
            right=store[index]  if index<n else store[-1]
            max_diff=max(max_diff,abs(nums1[i]-nums2[i])-min(abs(left-nums2[i]),abs(right-nums2[i])))
    return (res-max_diff)%modulo
A=[1,28,21]
B=[9,21,20]
print(minAbsoluteSumDiff(A,B))
         
