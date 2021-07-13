def solution(A,B,n):
    i=0
    j=0
    m1=m2=-1
    count=0
    while count<n+1:
        count+=1
        if i==n:
            m1=m2
            m2=B[0]
        if j==n:
            m1=m2
            m2=A[0]
        if A[i]<=B[j]:
            m1=m2
            m2=A[i]
            i+=1
        else:
            m1=m2
            m2=B[j]
            j+=1
    return (m1+m2)//2
            
    
    
if __name__=='__main__':
    ar1 = [1, 12, 15, 26, 38]
    ar2 = [2, 13, 17, 30, 45]
    n=len(ar1)
    m=len(ar2)
    if n==m:
        print(solution(ar1,ar2,n))
