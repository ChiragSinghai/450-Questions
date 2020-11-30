#the optimal solution for this question is
#kadane's algorithm
def kadane(arr, n):
    max_sum = arr[0]
    current_sum = max_sum
    for i in range(1, n):
        current_sum = max(current_sum + arr[i], arr[i])
        max_sum = max(current_sum, max_sum)
    return max_sum


def bruteforceapproach(A,n):
    max_sum=A[0]
    for i in range(0,n):
        j=i+1
        current_sum=A[i]
        while j<n:
            current_sum+=A[j]
            
            if current_sum>max_sum:
                max_sum=current_sum
            j+=1
        
    return max_sum
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        #arr=[-1, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
        print(kadane(arr,n))
        print(bruteforceapproach(arr,n))
