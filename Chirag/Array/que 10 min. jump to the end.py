def getJump(arr,n):
    if n==1:
        return 0
    if arr[0]==0:
        return -1
    indexreach=arr[0]
    jump=1
    steps=arr[0]
    for i in range(1,n):
        print(i)
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
            



# python program to count Minimum number 
# of jumps to reach end 

# Returns minimum number of jumps to reach arr[n-1] from arr[0] 
def minJumps(arr, n): 
# The number of jumps needed to reach the starting index is 0 
    if (n <= 1): 
            return 0

    # Return -1 if not possible to jump 
    if (arr[0] == 0): 
            return -1

    # initialization 
    # stores all time the maximal reachable index in the array 
    maxReach = arr[0] 
    # stores the amount of steps we can still take 
    step = arr[0] 
    # stores the amount of jumps necessary to reach that maximal reachable position 
    jump = 1

    # Start traversing array 

    for i in range(1, n):
            print(i)
            # Check if we have reached the end of the array 
            if (i == n-1): 
                return jump 

            # updating maxReach 
            maxReach = max(maxReach, i + arr[i]) 

            # we use a step to get to the current index 
            step -= 1; 

            # If no further steps left 
            if (step == 0): 
            # we must have used a jump 
                jump += 1
                    
            # Check if the current index / position or lesser index 
            # is the maximum reach point from the previous indexes 
                if(i >= maxReach): 
                    return -1

            # re-initialize the steps to the amount 
            # of steps to reach maxReach from position i. 
                step = maxReach - i;
    return -1


# Driver program to test above function 
arr = [1,4,0,2,0,1,3,0,1,1,4,5,9,10,11] 
size = len(arr) 

# Calling the minJumps function 
print("Minimum number of jumps to reach end is % d " % minJumps(arr, size)) 
print(getJump(arr,size))
# This code is contributed by Aditi Sharma 

        
        
