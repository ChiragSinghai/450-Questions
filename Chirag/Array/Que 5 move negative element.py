
arr=list(map(int,input().split()))
right=len(arr)-1
left=0
while left<=right:
    if arr[left]<0 and arr[right]<0:
        left+=1

    elif arr[left]<0 and arr[right]>=0:
        right-=1
        left+=1
    elif arr[left]>0 and arr[right]>=0:
        right-=1
    else:
        arr[left],arr[right]=arr[right],arr[left]
        right-=1
        left+=1
print(arr)
