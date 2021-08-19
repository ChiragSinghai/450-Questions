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
class Solution1:
    def grayCode(self, n) :        
        tab=[0]
        x=0
        while x<n:
            b=1<<x
            for i in range(b-1,-1,-1):
                tab.append(b|tab[i])
            x+=1
        return tab
    
obj=Solution1()
print(obj.grayCode(4))
