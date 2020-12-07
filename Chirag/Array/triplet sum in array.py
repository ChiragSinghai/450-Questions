def findtriplet(A,s):
    n=len(A)
    A.sort()
    for i in range(0,n-2):
        l=i+1
        r=n-1
        while l<r:
            m=A[i]+A[l]+A[r]
            if m==s:
                return True
            elif m<s:
                l+=1
            else:
                r-=1
    return False

    
if __name__=='__main__':
    A=[1, 4, 45, 6, 10, 8]
    s=22
    print('Yes' if findtriplet(A,s) else 'No')
    
