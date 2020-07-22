class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set();
        def findAre(i, j):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in seen and grid[i][j]):
                return 0;
            seen.add((i, j));
            return(1 + findAre(i + 1, j) + findAre(i - 1, j) + findAre(i, j + 1) + findAre(i, j - 1));
    
        ans = 0;
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans, findAre(i, j));
        return ans;

#If we are on a land square and explore every square connected to it 
#4-directionally (and recursively squares connected to those squares, 
#and so on), then the total number of squares explored will be the area 
#of that connected shape.
#
#To ensure we don't count squares in a shape more than once, let's use 
#seen to keep track of squares we haven't visited before. It will also 
#prevent us from counting the same shape more than once.
#
