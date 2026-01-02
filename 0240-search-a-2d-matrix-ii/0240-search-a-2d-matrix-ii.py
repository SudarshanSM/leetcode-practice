class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        columns=len(matrix[0])
        r=0
        c=columns-1
        while r < row and c >=0:
            value=matrix[r][c]
            if value==target:
                return True
            elif target > value:
                r+=1
            else:
                c-=1
        return False
            