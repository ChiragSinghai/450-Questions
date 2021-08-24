def kConcatenationMaxSum(arr,k):
    def k1(arr):
        curr=arr[0]
        maxsum=arr[0]
        for i in arr[1::]:
            if curr>=0:
                curr+=i
            else:
                curr=i
            maxsum=max(maxsum,curr)
        return maxsum
    
    def k2(arr):
        m= k1(arr[::]*2)
        s=sum(arr)
        if s<0:
            if m<0:
                return 0
            return m
        else:
            return m+(k-2)*s
    if k==1:
        return k1(arr)%(10**9+7)
    else:
        return k2(arr)%(10**9+7)
