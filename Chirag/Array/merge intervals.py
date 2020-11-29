def merger(A):
    A=sorted(A,key=lambda x:x[0])
    ans=[A[0]]
    for i in range(1,len(A)):
        print(ans)
        if A[i][0]<=ans[-1][1]:
            ans[-1][0]=min(A[i][0],ans[-1][0])
            ans[-1][1]=max(A[i][1],ans[-1][1])
        else:
            ans.append(A[i])
    return ans

if __name__=='__main__':
    A=[[1,3],[2,6],[8,10],[15,18]]
    print(merger(A))
