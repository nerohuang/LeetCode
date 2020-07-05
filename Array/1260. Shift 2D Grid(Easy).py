class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        originRow = len(grid);
        originCol = len(grid[0]);
        result = [[0] * originCol for _ in range(originRow)]
        for row in range(originRow):
            for col in range(originCol):
                newCol = (col + k) % originCol;
                countAddRow = (col + k) // originCol;
                newRow = (row + countAddRow) % originRow;
                result[newRow][newCol] = grid[row][col];
            
        return result;

##from itertools import chain
##
##class Solution:
##    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
##        y = len(grid)
##        x = len(grid[0])
##        grid_unwound = list(chain.from_iterable(grid))
##        shift_amount = k % len(grid_unwound)
##        shifted_grid = grid_unwound[-shift_amount:] + grid_unwound[:-shift_amount]
##        result = [[shifted_grid[i] for i in range(n*x,n*x+x)] for n in range(y)]
##        return result