class Solution():
    def searchMatrix(self, matrix, target):
        r=len(matrix)
        if r==0:
            return False
        c=len(matrix[0])-1
        print(c)
        check=-1
        for i in range(r):
            if matrix[i][0]==target:
                return True
            elif matrix[i][0]>target:
                check=i-1
                break
        else:
            return False
        print(check)
        i=0
        while i<c:
            mid=(c+i)//2
            print(mid)
            if matrix[check][mid]==target:
                return True
            elif matrix[check][mid]<target:
                i=mid+1
            else:
                c=mid-1
            print(c,i,mid)
        return False

matrix=[[]]
target=16
obj=Solution()
print(obj.searchMatrix(matrix,target))
