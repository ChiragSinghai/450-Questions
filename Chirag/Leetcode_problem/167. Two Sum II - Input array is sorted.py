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

print(twoSum([1,2,3,4,5,7,9,11],9))
