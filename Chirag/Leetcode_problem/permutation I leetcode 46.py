def permute(L):
    result=[]
    if len(L)==1:
        return [L[:]]
    for i in range(len(L)):
        n = L.pop(0)
        perms=permute(L)
        #print(perms)
        for per in perms:
            per.append(n)
        #print(perms)

        result.extend(perms)
        L.append(n)
    print(result)
    return result


A=[1,2,3]
print(permute(A))

def to_string(A):
    return ''.join(A)

def permute(A,l,r):
    if l==r:
        print(to_string(A))
    else:
        for i in range(l,r+1):
            A[l],A[i]=A[i],A[l]
            permute(A,l+1,r)
            A[l],A[i]=A[i],A[l]

A='ABC'
A=list(A)
n=len(A)-1
permute(A,0,n)
    
