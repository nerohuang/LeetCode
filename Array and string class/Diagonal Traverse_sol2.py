class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        m, n = len(matrix), len(matrix[0])
        
        d = collections.defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                d[i+j].append(matrix[i][j])
        
        zz = False
        
        for key, value in d.items():
            result.extend(value if zz else value[::-1])
            zz = not zz
        
        return result