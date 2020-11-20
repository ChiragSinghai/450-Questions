def reverse(a):
    start_index=0
    end_index=len(a)-1
    while start_index<end_index:
        a[end_index],a[start_index]=a[start_index],a[end_index]
        end_index-=1
        start_index+=1
        print(end_index,start_index)
    print(a)
#another approach
def another_reverse(a):
    n=len(a)//2
    for i in range(1,n):
        a[i],a[-i-1]=a[-i-1],a[i]
    a[0],a[-1]=a[-1],a[0]
    print(a)



if __name__=='__main__':
    arr=input().split()
    '''do not use both function at the same time otherwise the array will
    remain same due to the memory location'''
    
    #reverse(arr)
    another_reverse(arr)
