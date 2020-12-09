def getsubarray(A,s):
    n=len(A)
    start=end=0
    cur_sum=0
    min_len=n+1
    while end<n:
        while cur_sum<=s and end<n:
            cur_sum+=A[end]
            end+=1
        while start<n and cur_sum>s:
            if end-start<min_len:
                min_len=end-start
            cur_sum-=A[start]
            start+=1
    print(min_len)
        
if __name__=='__main__':
    getsubarray([1, 10, 5, 2, 7]  ,9)
    
