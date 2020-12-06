def find(A,n):
    l=[]
    mi=ma=A[0]
    for i in range(1,n):
        if A[i]<mi or ma>A[i]:
            if ma-mi>0:
                l.append(ma-mi)
            ma=A[i]
            mi=A[i]
        else:
            if A[i]>ma:
                ma=A[i]
        print(mi,ma)
    if ma-mi>0:
        l.append(ma-mi)
    print(l)

if __name__=='__main__':
    A=[5,25,3,28,27,4,29,30,32,5,6]
    find(A,len(A))
        
