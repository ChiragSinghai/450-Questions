def get_gap(gap):
    if gap<=1:
        return 0
    return (gap//2)+gap%2
def merge(A,B,n,m):
    s=n+m
    gap=get_gap(s)
    while gap>0:
        #print(gap)
        i=0
        while i + gap < n:
            
            if (A[i] > A[i + gap]):
                A[i], A[i + gap] = A[i + gap], A[i]
            i += 1    
        j = gap - n if gap > n else 0
        print(j)
        while i < n and j < m:
            if (A[i] > B[j]):
                A[i], B[j] = B[j], A[i]
            i += 1
            j += 1
            
        if (j < m):
            j = 0
            while j + gap < m :
                if (B[j] > B[j + gap]):
                    B[j], B[j + gap] = B[j + gap], B[j]
                j += 1
        gap = get_gap(gap)
if __name__=='__main__':
    N=int(input())
    M=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    merge(A,B,N,M)
    for i in A:
        print(i)
    for i in  B:
        print(i)
    
