def permuteUnique(nums):
    res=[]
    perms=[]
    count = {n:0 for n in nums}
    for n in nums:
        count[n]+=1
    print(count)
    def dfs():
        if len(perms)==len(nums):
            res.append(perms[:])
            #print('return')
            return

        for n in count:
            if count[n]>0:
                perms.append(n)
                count[n]-=1
                #print(perms)
                dfs()
                #print(n,count[n])
                count[n]+=1
                perms.pop()
    dfs()
    return res

print(permuteUnique([1,1,1,2]))
