class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid);
        n = len(grid[0]);
        x = m - 1;
        y = 0;
        ans = 0;
        while x >= 0 and y < n:
            if grid[x][y] < 0:
                ans += n - y;
                x -= 1;
            else:
                y += 1;
        return ans;


#  Please refer to the perspicacious elaboration from @ikeabord as follows:
#  This solution uses the fact that the negative regions of the matrix will form a "staircase" shape, e.g.:
#  
#  ++++++
#  ++++--
#  ++++--
#  +++---
#  +-----
#  +-----
  

#class Solution:
#    def countNegatives(self, grid: List[List[int]]) -> int:
#        
#        count = 0
#        for x in grid:
#            for index in x:
#                if index < 0:
#                    count += 1
#        
#        return count