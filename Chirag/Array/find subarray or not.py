def find(A,B,m,n):
    d={}
    for i in B:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(d)
    for i in A:
        if i in d:
            d[i]-=1
            if d[i]==0:
                d.pop(i)
    if len(d)>0:
        return 0
    else:
        return 1
              
'''
3
6 4
11 1 13 21 3 7
11 3 7 1
6 3
1 2 3 4 5 6
1 2 4
5 3
10 5 2 23 19
19 5 3
'''
if __name__=='__main__':
    for _ in range(int(input())):
        m,n=map(int,input().split())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        print('Yes' if find(A,B,m,n) else 'NO')
