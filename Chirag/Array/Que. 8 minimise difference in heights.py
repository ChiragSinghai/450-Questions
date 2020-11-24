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


# Python 3 program to find the minimum 
# possible difference between maximum 
# and minimum elements when we have to 
# add / subtract every number by k 

# Modifies the array by subtracting / 
# adding k to every element such that 
# the difference between maximum and 
# minimum is minimized 
def getMinDiff(arr, n, k): 

	if (n == 1): 
		return 0

	# Sort all elements 
	arr.sort()
	print(arr)

	# Initialize result 
	ans = arr[n-1] - arr[0] 

	# Handle corner elements 
	small = arr[0] + k 
	big = arr[n-1] - k 
	
	if (small > big): 
		small, big = big, small 

	# Traverse middle elements 
	for i in range(1, n-1): 
	
		subtract = arr[i] - k 
		add = arr[i] + k 

		# If both subtraction and addition 
		# do not change diff 
		if (subtract >= small or add <= big): 
			continue

		# Either subtraction causes a smaller 
		# number or addition causes a greater 
		# number. Update small or big using 
		# greedy approach (If big - subtract 
		# causes smaller diff, update small 
		# Else update big) 
		if (big - subtract <= add - small): 
			small = subtract 
		else: 
			big = add 
	

	return min(ans, big - small) 


# Driver function 
arr =[6,1,9,1,1,7,9,5,2,10]
 
n = len(arr) 
k = 4

print("Maximum difference is", getMinDiff(arr, n, k)) 

# This code is contributed by 
# Smitha Dinesh Semwal 

'''
for _ in range(int(input())):
    #k=int(input())
    #A=list(map(int,input().split()))
    k=4
    A=[6,1,9,1,1,7,9,5,2,10]

    solution(A,len(A),k)
'''
