def solution(A):
    n=len(A)
    index=n//2
    if n==1:
        return A[0]
    if n==2:
        return (A[0]+A[1])//2
    for i in range(index+1):
        m=i+1
        for j in range(m+1,n):
            if A[m]>A[j]:
                m=j
        if A[m]<A[i]:
            A[i],A[m]=A[m],A[i]
    if n%2==0:
        return (A[index]+A[index-1])//2
    else:
        return A[index]
        
if __name__=='__main__':
    print(solution([4,5,6,7,2,3]))
