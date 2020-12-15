class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        presum = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))];
        
        presum[0][0] = grid[0][0];
        
        for i in range(1, len(grid[0])):
            presum[0][i] = presum[0][i - 1] + grid[0][i];
        
        for i in range(1, len(grid)):
            presum[i][0] = presum[i - 1][0] + grid[i][0];
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                presum[i][j] = min(presum[i - 1][j], presum[i][j - 1]) + grid[i][j];
            
        return(presum[-1][-1])

#思路：
#先建立第一行的presum和第一列的presum
#然后从第二行开始遍历:
#取grid[i][j]上面和左面比较小的presum：min(presum[i - 1][j], presum[i][j - 1])
#然后加上grid[i][j]然后并存入presum[i][j]；
#最后一格就是结果