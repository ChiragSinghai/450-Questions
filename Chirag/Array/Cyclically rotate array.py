#to rotate a array by one it you can just
#swap the first element and last element
def rotateByOne(a,n):
    tmp=a[0]
    for i in range(1,n):
        prev=tmp
        tmp=a[i]
        a[i]=prev
    a[0]=tmp
    return a
if __name__=='__main__':
    n=int(input())
    A=input().split()
    a=(rotateByOne(A,n))
    print(' '.join(a))    
    
    
    
