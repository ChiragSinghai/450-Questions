def trapwater(A):
    maxLeft=A[0]
    n=len(A)
    maxRight=A[-1]
    trapwater=0
    i=1
    j=n-2
    while i<=j:
        if maxLeft<=maxRight:

            if A[i]<maxLeft:
                trapwater+=maxLeft-A[i]
            else:
                maxLeft=A[i]
            i+=1
        else:
            if A[j]<maxRight:
                trapwater+=maxRight-A[j]
            else:
                maxRight=A[j]
            j-=1
        #print(maxLeft,maxRight)
    print(trapwater)
    
if __name__=='__main__':
    structure=[3, 0, 2, 0, 4]
    structure1=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    trapwater(structure1)
