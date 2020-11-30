def count_inversion(A,n):
    start=0
    end=n-1
    global count
    count=0
    merge_sort(A,start,end)
    print(count)
def merge(A,start,mid,end):
    global count
    temp=[0 for i in range(end-start+1)]
    i,j,k=start,mid+1,0
    while i<=mid and j <=end:
        if A[i]<=A[j]:
            temp[k]=A[i]
            i+=1
            
        else:
            A[k]=A[j]
            j+=1
            count+=mid-i+1
        k+=1
    while i<=mid:
        temp[k]=A[i]
        i+=1
        k+=1
    while j<=end:
        temp[k]=A[j]
        j+=1
        k+=1

    for i in range(start,end+1):
        A[i]=temp[i-start]
        
def merge_sort(A,start,end):
    if start<end:
        mid=(start+end)//2
        merge_sort(A,start,mid)
        merge_sort(A,mid+1,end)
        merge(A,start,mid,end)

if __name__=='__main__':
    #N=int(input())
    N=5
    #A=list(map(int,input().split()))
    A=[1,2,3,4,5]
    count_inversion(A,N)
        
