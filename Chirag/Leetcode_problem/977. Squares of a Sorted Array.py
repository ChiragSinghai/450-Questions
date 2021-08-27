def sortedSquares(nums):
    L=0
    R=len(nums)-1
    A=[0]*(R+1)
    for i in range(R,-1,-1):
        if abs(nums[L])>abs(nums[R]):
            A[i]=nums[L]**2
            L+=1
        else:
            A[i]=nums[R]**2
            R-=1
    
    return A
def sortedSquares1(nums):
    A=[]
    for i in nums:
        A.append(i**2)
    return sorted(A)


A=[-4,-1,0,3,10]
B=[-7,-3,2,3,11]
print(sortedSquares1(A))
print(sortedSquares(B))
