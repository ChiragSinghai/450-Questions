def part(A,s):
    high=s[1]
    low=s[0]
    n=len(A)
    start=0
    end=n-1
    mid=0
    while mid<=end:
        if A[mid]<low:
            A[start],A[mid]=A[mid],A[start]
            start+=1
            mid+=1
        elif A[mid]>high:
            A[end],A[mid]=A[mid],A[end]
            end-=1
        else:
            mid+=1
    print(A)
    #O(n)
def brutual(A,s):
    A.sort()
    print(A)
    #O(nlogn)
if __name__=='__main__':
    part([1,25,8,3,9,12,4,8,0,2,7,11],(3,9))
    #brutual([1,25,8,3,9,12,4,8,0,2,7,11],(3,9))
