class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=0
        c=len(matrix[0])-1
        rows=len(matrix)
        while r<rows and c>=0:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                c-=1
            else:
                r+=1
        return False
