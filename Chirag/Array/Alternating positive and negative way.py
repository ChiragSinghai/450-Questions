def arrange(A,n):
    check=-1
    for i in range(n):
        if check>=0:
            if (A[i]>=0 and A[check]<0) or (A[i]<0 and A[check]>=0):
                A=rotate(A,n,i,check)
                if i-check >= 2:
                    check+=2
                else:
                    check=-1
        else:
            if (A[i]>=0 and i%2==0) or (A[i]<0 and i%2==1):
                check=i
    return A
        
def rotate(A,n,i,check):
    temp=A[i]
    for j in range(i,check,-1):
        A[j]=A[j-1]
    A[check]=temp
    print(A)
    return A


if __name__=='__main__':
    A=[-5,4,3,2,-1,6,-7]
    A=arrange(A,len(A))
    print(A)
    print(arrange([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8],10))
      
