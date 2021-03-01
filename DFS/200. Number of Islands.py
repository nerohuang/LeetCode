def numIslands(self, grid: List[List[str]]) -> int:
        
        def backtrack(grid,i,j,r,c):
            
            if i>=r or j>=c or i<0 or j<0:
                return
            
            if grid[i][j]=="2" or grid[i][j]=="0":
                return
            
            grid[i][j]="2"
            
            backtrack(grid,i+1,j,r,c)
            backtrack(grid,i-1,j,r,c)
            backtrack(grid,i,j+1,r,c)
            backtrack(grid,i,j-1,r,c)
            
            return              
            
        r = len(grid)
        c = len(grid[0])
        
        total = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    backtrack(grid,i,j,r,c)
                    total+=1
        
        return total

# 思路：
# 鸡贼啊，说好的DP呢，最后他妈是个DFS
# 所以其实就是在一个坐标如果是1，那么开始便利他上下左右
# 遍历过的坐标变为2。 当遍历到坐标为2或0表示
# 已经遍历过了或者不是陆地了，就停止。
# 然后总岛数 +1