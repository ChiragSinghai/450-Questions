def find(hist):
    left=[]
    right=[]
    max_area = 0
    n = len(hist)
    stack = []
    
    for i in range(n):
        done = False
        while stack and not done:
            top=stack.pop()
            if hist[top]<hist[i]:
                left.append(top+1)
                done = True
                stack.append(top)
                stack.append(i)
                
                
        if not done:
            left.append(0)
            stack.append(i)
    stack.clear()
    for i in range(n-1,-1,-1):
        
        done = False
        while stack and not done:
            top=stack.pop()
            if hist[top]<hist[i]:
                right.append(top-1)
                done = True
                stack.append(top)
                stack.append(i)
        if not done:
            stack.append(i)
            right.append(n-1)
    right.reverse()
    for i in range(n):
        max_area = max(max_area,(right[i]-left[i]+1)*hist[i])
    print(max_area)

def findarea(A):
    maxarea = 0
    hstack=[]
    pstack=[]
    #A.append(0)
    n=len(A)
    for i in range(n):
        lastwidth=n*n+1
        while hstack and hstack[-1]>A[i]:
            lastwidth = pstack[-1]
            currarea = (i-pstack.pop())*hstack.pop()
            maxarea=max(maxarea,currarea)
            
        if not hstack or hstack[-1]<A[i]:
            hstack.append(A[i])
            pstack.append(min(lastwidth,i))
        print(hstack,pstack,maxarea)
    while pstack:
        currarea = (n-pstack.pop())*hstack.pop()
        maxarea=max(currarea,maxarea)
    print(maxarea)
    
if __name__=='__main__':
    A=[2,2,1,3,4,1,2]
    #A = [2,1,5,6,2,3]
    findarea(A)
