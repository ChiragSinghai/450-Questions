class Solution(object):
    def searchMatrix(self, matrix, target):
        r=len(matrix)
        c=len(matrix[0])-1
        if r==1 and c==-1:
            return False
        check=-1
        for i in range(r):
            if matrix[i][0]<=target and matrix[i][c]>=target:
                check=i
                break
        else:
            return False
        print(check)
        i=0
        while i<=c:
            mid=(c+i)//2
            #print(mid)
            if matrix[check][mid]==target:
                return True
            elif matrix[check][mid]<target:
                i=mid+1
            else:
                c=mid-1
            print(c,i,mid)
        return False
                

matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target=143
obj=Solution()
print(obj.searchMatrix(matrix,target))
