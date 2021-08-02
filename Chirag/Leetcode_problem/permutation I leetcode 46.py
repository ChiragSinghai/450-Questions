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


A=[1,1,3]
print(permute(A))
