'''Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4'''
def bin_search(A,x,l,h):
    if l>h:
        return -1
    mid=(l+h)//2
    if A[mid]==x:
        return mid
    if A[l]<=A[mid]:
        if A[l]<=x and A[mid]>=x:
            return bin_search(A,x,l,mid-1)
        return bin_search(A,x,mid+1,h)
    if A[mid]<=x and A[h]>=x:
        return bin_search(A,x,mid+1,h)
    return bin_search(A,x,l,mid-1)
        

if __name__=='__main__':
    S=input()
    target=int(input())
    A=list(map(int,S[1:-1].split(',')))
    n=len(A)
    #if target<A[0] and target>A[n-1]:
    #    print(-1)
    #else:
    print(bin_search(A,target,0,n-1))
    
