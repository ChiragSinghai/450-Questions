def maxSumOfThreeSubarrays(nums, k):
    n=len(nums)
    left=[0]*n
    right=[0]*n
    s=0
    prefix=[0]*n
    for i in range(n):
        if i==0:
            prefix[i]=nums[i]
        else:
            prefix[i]=prefix[i-1]+nums[i]
    for i in range(n):
        if i<k:
            s+=nums[i]
            left[i]=s
        else:
            s+=nums[i]-nums[i-k]
            left[i]=max(left[i-1],s)
    s=0
    for i in range(n-1,-1,-1):
        if i+k>=n:
            s+=nums[i]
            right[i]=s
        else:
            s+=nums[i]-nums[i+k]
            right[i]=max(s,right[i+1])
    ans=0
    in_1=-1
    in_2=-1
    in_3=-1
    for i in range(k,n-(2*k)+1):
        if left[i-1]+right[i+k]+(prefix[i+k-1]-prefix[i-1])>ans:
            in_1=left[i-1]
            in_2=(prefix[i+k-1]-prefix[i-1])
            in_3=right[i+k] 
            ans=left[i-1]+right[i+k]+(prefix[i+k-1]-prefix[i-1])
    
    A=[]
    print(in_1,in_2,in_3)
    for i in range(n-(2*k)):
        if left[i]==in_1:
            A.append(i-k+1)
            break
    for i in range(A[-1]+k,n-(2*k)+1):
        if (prefix[i+k-1]-prefix[i-1])==in_2:
            A.append(i)
            break
    for i in range(A[-1]+k,n):
        if prefix[i+k-1]-prefix[i-1]==in_3:
            A.append(i)
            break
    return sorted(A)

