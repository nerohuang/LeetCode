class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix or not matrix[0]: return ans
        m, n = len(matrix), len(matrix[0])
        for k in range(m+n-1):
            if k % 2 == 0:
                if k < m:
                    i = k
                    j = 0
                else:
                    i = m-1
                    j = k-i
                while i>=0 and j<n:
                    #print(i, j)
                    ans.append(matrix[i][j])
                    i -= 1
                    j += 1
            else:
                if k < n:
                    j = k
                    i = 0
                else:
                    j = n-1
                    i = k-j
                while i<m and j>=0:
                    #print(k, i, j, matrix[i][j])
                    ans.append(matrix[i][j])
                    i += 1
                    j -= 1
        return ans