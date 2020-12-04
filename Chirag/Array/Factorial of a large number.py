'''In python to get factorial is a easy way but in C/C++ the size
the variable is limited so the solution is according to the c/C++ approach'''
def Fact(n):
    q=2
    A=[0]*10000
    l=1
    A[0]=1
    while q<=n:
        x=0
        num=0
        while x<l:
            A[x]=A[x]*q
            A[x]=A[x]+num
            num=A[x]//10
            A[x]=A[x]%10
            x+=1
        while num!=0:
            A[l]=num
            num=num//10
            l+=1
        q+=1
    l-=1
    while l>=0:
        print(A[l],end='')
        l-=1
if __name__=='__main__':
    Fact(100)
        
