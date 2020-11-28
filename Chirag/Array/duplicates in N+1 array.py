'''Input:
N
a1,a2,a3...aN+1
'''
def Solution(A):
    L=[]
    for i in A:
        if i in L:
            return i
        else:
            L.append(i)
    return -1

def Solution1(A,N):
    A.sort()
    for i in range(N):
        if A[i]==A[i+1]:
            return A[i]
    return -1
#most important approach
def Floyd_Algorithm(A,N):
    tortoise=hare=0
    try:
        while A[hare]:
            tortoise=A[tortoise]
            hare=A[A[hare]]
            #print(tortoise,hare)
            if tortoise==hare:
                tortoise=A[0]
                while True:
                    tortoise=A[tortoise]
                    hare=A[hare]
                    if hare==tortoise:
                        return hare
    except IndexError:
        return -1
if __name__=='__main__':
    N=int(input())
    arr=list(map(int,input().split()))
    print(Solution(arr))
    print(Solution1(arr,N))
    print(Floyd_Algorithm(arr,N))
