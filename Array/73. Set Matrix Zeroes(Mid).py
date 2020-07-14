class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix);
        m = len(matrix[0])
        zeroLoc = [];
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeroLoc.append([i, j]);
        for x, y in zeroLoc:
            for i in range(m):
                matrix[x][i] = 0;
            for i in range(n):
                matrix[i][y] = 0;

#class Solution:
#    def setZeroes(self, matrix: List[List[int]]) -> None:
#        """
#        Do not return anything, modify matrix in-place instead.
#        """
#        rows = len(matrix)
#        cols = len(matrix[0])
#        R, C = set(), set()
#        for i in range(rows):
#            for j in range(cols):
#                if matrix[i][j] == 0:
#                    R.add(i)
#                    C.add(j)
#                    
#        for i in range(rows):
#            for j in range(cols):
#                if i in R or j in C:
#                    matrix[i][j] = 0