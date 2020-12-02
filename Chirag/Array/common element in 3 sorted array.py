def search(A,B,C,x,y,z):
    res=[]
    i=j=k=0
    
    while i < x and j < y and k < z:
        if A[i]==B[j]==C[k]:
            res.append(A[i])
            i+=1
            j+=1
            k+=1
        elif min(A[i],B[j],C[k])==A[i]:
            i+=1
        elif min(A[i],B[j],C[k])==B[j]:
            j+=1
        else:
            k+=1
    return res
    

if __name__=='__main__':
    A=[4,5,6,8,9]
    B=[1,2,4,6,10]
    C=[0,3,4,6]
    print(search(A,B,C,len(A),len(B),len(C)))
