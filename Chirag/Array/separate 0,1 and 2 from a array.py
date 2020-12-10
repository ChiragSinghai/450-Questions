def sorting(A):
    n=len(A)
    start=0
    end=n-1
    mid=0
    while mid<=end:
        if A[mid]==0:
            A[start],A[mid]=A[mid],A[start]
            start+=1
            mid+=1
        elif A[mid]==1:
            #A[mid],A[mid]=A[mid],A[mid]
            mid+=1
        else:
            A[end],A[mid]=A[mid],A[end]
            end-=1
    print(A)


            
if __name__=='__main__':
    sorting([1,2,1,2,0,0,0,2,1,1,2,0])
