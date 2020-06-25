class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False;
        return True;

##class Solution:
##    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
##        if not matrix:
##            return False
##        rows = len(matrix)
##        cols = len(matrix[0])
##        
##        for y in range(rows-1):
##            for x in range(cols-1):
##                if matrix[y][x] != matrix[y+1][x+1]:
##                    return False
##        return True
    