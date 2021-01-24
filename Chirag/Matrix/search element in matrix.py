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
                
class Solution1():
    def searchMatrix(self, matrix, target):
        r=len(matrix)
        if r==0:
            return False
        c=len(matrix[0])
        if r==1 and c==0:
            return False
        m=r*c
        m-=1
        i=0
        while i<=m:
            mid=(m+i)//2
            row=mid//c
            column=mid%c
            #print(mid)
            if matrix[row][column]==target:
                return True
            elif matrix[row][column]<target:
                i=mid+1
            else:
                m=mid-1
            #print(c,i,mid)
        return False
                
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target=300
obj=Solution1()
print(obj.searchMatrix(matrix,target))
