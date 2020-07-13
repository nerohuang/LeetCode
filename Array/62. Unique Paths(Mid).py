class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[1] * m for _ in range(n)];
        for i in range(1, n):
            for j in range(1, m):
                path[i][j] = path[i - 1][j] + path[i][j - 1];
        return(path[n - 1][m - 1]);

#class Solution:
#    def uniquePaths(self, m: int, n: int) -> int:
#        def choose(n, m):
#            ans = 1
#            for i in range(1, m + 1):
#                ans = ans * (n + 1 - i) // i
#            return ans
#        
#        return choose(m-1+n-1, m-1)
        