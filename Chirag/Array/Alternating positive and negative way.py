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
#Second Approach via quick sort technique
def quick_sort_partition(A,end):
    neg=-1
    pivot=0
    for pos in range(end):
        if A[pos]<pivot:
            neg+=1
            A[neg],A[pos]=A[pos],A[neg]
    l=1
    p=neg+1
    while l<neg and p<end:
        A[l],A[p]=A[p],A[l]
        l+=2
        p+=1
    print(A)
    
    
        


if __name__=='__main__':
    A=[-5,4,3,2,-1,6,-7]
    A=arrange(A,len(A))
    print(A)
    print(arrange([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8],10))
    quick_sort_partition(A,len(A))

      
