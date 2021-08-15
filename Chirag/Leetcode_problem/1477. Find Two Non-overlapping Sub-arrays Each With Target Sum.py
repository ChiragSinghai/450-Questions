def minSumOfLengths(arr,target):
    D={0:-1}
    n=len(arr)
    dp1=[0]*n
    dp2=[0]*n
    currsum=0
    prefix=[0]*n
    for i in range(n):
        prefix[i]=arr[i] if not i else arr[i]+prefix[i-1]
        l=n+1
        req=prefix[i]-target
        if req in D:
            l=i-D[req]
        D[prefix[i]]=i
        dp1[i]=min(l,dp1[i-1] if i!=0 else l )
    print(prefix)
    D={0:n}
    for i in range(n-1,-1,-1):
        prefix[i]=arr[i] if i==n-1 else arr[i]+prefix[i+1]
        l=n+1
        req=prefix[i]-target
        if req in D:
            l=D[req]-i
        D[prefix[i]]=i
        dp2[i]=min(l,dp2[i+1] if i!=n-1 else l )
    res=float("inf")
    for i in range(n-1):
        res=min(res,dp1[i]+dp2[i+1])
    
    return res if res<=n else -1

def minSumOfLengths1( arr, target):
    result = inf = 2**31-1
    i = window = count = 0
    # preMin: store (index, previous shortest length)
    preMin = [(-1, inf)]

    # i: window start, j: window end
    for j, num in enumerate(arr):
        window += num
        while window > target:
            window -= arr[i]
            i += 1
        
        if window == target:
            print('j:',j,i)
            curr = j - i + 1
            if curr == 1: 
                count += 1
                if count == 2: print('eh');return 2
            n = 0 
            for index, length in preMin[::-1]:
                if index <= i-1:
                    print(i,index,length)
                    n = length           
                    break
			
            print("before",result)
            if result > curr + n: result = curr + n
            print("after",result)
            print("before",preMin)
            if curr < preMin[-1][-1]: preMin.append((j, curr))
            print("after",preMin)
    return result if result < inf else -1
print(minSumOfLengths1([2,1,3,3,1,2,3],6))
