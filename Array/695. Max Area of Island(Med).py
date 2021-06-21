class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def findAre(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1):
                return 0;
            grid[i][j] = 0
            return(1 + findAre(i + 1, j) + findAre(i - 1, j) + findAre(i, j + 1) + findAre(i, j - 1));
    
                    
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans, findAre(i, j));
        return ans; 

# 思路
# 是个DFS，就是一路往上下左右找，为了防止是找过的，那么走过为1的空格就变成1
# 其他没什么要注意的了