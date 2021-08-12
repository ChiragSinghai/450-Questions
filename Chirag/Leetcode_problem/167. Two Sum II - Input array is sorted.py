def twoSum(numbers,target):
    l=0
    r=len(numbers)-1
    while l<r:
        cursum=numbers[l]+numbers[r]
        if cursum>target:
            r-=1
        elif cursum<target:
            l+=1
        else:
            return [l+1,r+1]
def twoSum1(numbers,target):
    r=len(numbers)-1
    while numbers[r]>target and r>1:
        numbers.pop()
        r-=1
    D={}
    print(r)
    for i in range(0,r+1):
        
        diff=target-numbers[i]
        
        if diff in D:
            if D[diff]!=i:
                return [D[diff]+1,i+1]
        D[numbers[i]]=i
print(twoSum([1,2,3,4,5,7,9,11],9))
print(twoSum1([1,2,3,4,5,7,9,11],9))

