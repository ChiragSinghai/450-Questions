def Union(X,Y):
    U=[]
    m=len(X)
    n=len(Y)
    i=j=0
    while i<m and j<n:
        if X[i]<Y[j]:
            U.append(X[i])
            i+=1
        elif X[i]>Y[j]:
            U.append(Y[j])
            j+=1
        else:
            U.append(X[i])
            i+=1
            j+=1
    while i<m:
        U.append(X[i])
        i+=1
    while j<n:
        U.append(Y[j])
        j+=1
    return U

def Intersection(X,Y):
    I=[]
    m=len(X)
    n=len(Y)
    i=j=0
    while i<m and j<n:
        if X[i]<Y[j]:
            i+=1
        elif X[i]>Y[j]:
            j+=1
        else:
            I.append(X[i])
            i+=1
            j+=1
    
    return I
        
    

A=list(map(int,input().split()))
B=list(map(int,input().split()))

print(Union(A,B))
print(Intersection(A,B))
##print(UnionWithoutDuplicates(A,B))





