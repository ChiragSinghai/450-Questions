
def calculateSpan(A, n, ans):
    
    
    ans[0] = 1

    
    print(A)
    print(ans)
    for i in range(1, n):
            counter = 1
            
            while ((i - counter) >= 0 and
                    A[i] >= A[i - counter]):
                    print(i,counter)
                    counter += ans[i - counter]
                    print(counter)
            ans[i] = counter
            print(ans)


def printArray(arr, n):
    
    for i in range(n):
            print(arr[i], end = ' ')
    print()
def usestack(A,n,S):
    stack=[0]
    for i in range(1,n):
        print(S)
        while stack and A[stack[-1]]<=A[i]:
            print('here')
            stack.pop()
        if stack:
            S[i]=i-stack[-1]
        else:
            S[i]=i+1
        stack.append(i)
    

if __name__=='__main__':
    price = [ 10, 4, 5, 90, 120, 80 ]
    n = len(price)
    S = [0] * (n)
    S[0]=1

    
    #calculateSpan(price, n, S)
    usestack(price,n,S)
    
    printArray(S, n)

    
