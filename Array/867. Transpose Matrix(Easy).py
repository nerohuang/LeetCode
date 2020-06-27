class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        m = len(A);
        n = len(A[0]);
        result = [[None] * m for _ in range(n)];
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                result[c][r] = val;
        return result;

##class Solution:
##    def transpose(self, A: List[List[int]]) -> List[List[int]]:
##        matrix=[[0]*len(A) for _ in range(len(A[0]))]
##        print(matrix)
##        for i in range(len(A[0])):
##            for j in range(len(A)):
##                matrix[i][j]=A[j][i]
##        return matrix