def getJump(arr,n):
    if n==1:
        return 0
    if arr[0]==0:
        return -1
    indexreach=arr[0]
    jump=1
    steps=arr[0]
    for i in range(1,n):
        #print(i)
        if i == n-1:
            return jump
        if arr[i]+i>=n-1:
            return jump+1
        indexreach=max(indexreach,arr[i]+i)
        steps-=1
        if steps==0:
            jump+=1
            if indexreach<=0:
                return -1
            steps=indexreach-i
    return -1

def BrutualForceApproach(arr,n):
    if n==1:
        return 0
    if arr[0]==0:
        return -1
    jump=1
    for i in range(1,n):
        step=arr[i]
        if step+i==n-1:
            return jump+1
        j=i
        m=arr[j+1]
        j+=1
        step-=1
        while step:
            m=max(m,arr[j])
            step-=1
    return 
            
        
        
            




arr = [1,4,0,2,0,1,3,0,1,1,4,5,9,10,11] 
size = len(arr) 



        
        
