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
        
if __name__=='__main__':
    A = [2,1,5,6,2,3]
    find(A)
