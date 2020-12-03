def arrange(A,n):
    check=-1
    for i in range(n):
        if check>=0:
            if (A[i]>=0 and A[check]<0) and (A[i]<0 and A[check]>=0):
                
        else:
            if (A[i]>=0 and i%2==0) or (A[i]<0 and i%2==1):
                check=i
        
