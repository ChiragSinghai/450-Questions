def gray():
    tables=[[0,1]]
    for i in range(16):
        l=1<<(i+1)
        prev=tables[-1][:]
        for j in range(l-1,-1,-1):

            prev.append(l | tables[-1][j])
        tables.append(prev)
    return tables
class Solution:
    tab=gray()
    def grayCode(self, n):        
        return Solution.tab[n-1]
obj=Solution()
print(obj.grayCode(4))
