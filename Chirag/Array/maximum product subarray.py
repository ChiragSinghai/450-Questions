def find(A,n):
    minval=A[0]
    maxval=A[0]
    maxprod=A[0]
    for i in range(1,n):
        if A[i]<0:
            maxval,minval=minval,maxval
        maxval=max(A[i],maxval*A[i])
        minval=max(A[i],minval*A[i])
        maxprod=max(maxprod,maxval)
    return maxprod
        
if __name__=='__main__':
    print(find( [-1, -3, -10, 0, 60],5))
