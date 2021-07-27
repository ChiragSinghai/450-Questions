def getnum(A):
    n=len(A)
    for i in range(n):
        number = i^A[i]
    return number


if __name__=='__main__':
    A=[3,2,4,1]
    print(getnum(A))
