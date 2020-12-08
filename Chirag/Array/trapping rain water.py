def trap(A):
    n=len(A)
    lo=0
    hi=n-1
    mi=ans=ma=0
    while lo<=hi:
        if A[lo]<A[hi]:
            if A[lo]>mi:
                mi=A[lo]
            else:
                ans+=mi-A[lo]
            lo+=1
        else:
            if A[hi]>ma:
                ma=A[hi]
            else:
                ans+=ma-A[hi]
            hi-=1
    print(ans)
    
if __name__=='__main__':
    trap([7,4,0,9])
