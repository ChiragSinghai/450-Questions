def solution(arr,n,k):
    arr.sort()
    ans=arr[n-1]-arr[0]
    big=arr[n-1]-k
    small=arr[0]+k
    if small>big:
        big,small=small,big
    print(arr)
    for i in range(1,n-1):
        add=arr[i]+k
        sub=arr[i]-k
        if sub>=small or add<=big:
            continue
        if sub<=small and add>=big:
            continue
        print(':',sub,add,small,big,i)
        if abs(small-sub)<=abs(big-add):
            print('1',sub,small,arr[i])
            small=sub
        else:
            print('2',add,big,arr[i])
            big=add
    print(ans,big,small)
    ans=min(ans,big-small)
    print(ans)


for _ in range(int(input())):
    #k=int(input())
    #A=list(map(int,input().split()))
    k=4
    A=[6,1,9,1,1,7,9,5,2,10]

    solution(A,len(A),k)
