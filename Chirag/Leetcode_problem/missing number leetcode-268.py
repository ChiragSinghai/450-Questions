def getnum(A):
    n=len(A)
    number=0
    for i in range(n):
        number = number^i^A[i]
    number^=n
    return number


if __name__=='__main__':
    A=[3,2,1,4]
    print(getnum(A))
