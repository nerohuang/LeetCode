class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0;
        ans = 0;
        
        def magic(a, b, c, d, e, f, g, h, i):
            return(sorted([a, b, c, d, e, f, g, h, i]) == [1,2,3,4,5,6,7,8,9] and (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g == 15))
        
        for r in range(len(grid) - 2):
            for c in range(len(grid[r]) - 2):
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1;
        return ans;

##class Solution:
##    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
##        R, C = len(grid), len(grid[0])
##
##        def magic(a,b,c,d,e,f,g,h,i):
##            #print(a+b+c,d+e+f,g+h+i,a+d+g,b+e+h,c+f+i,a+e+i,c+e+g )
##            #print(sorted([a,b,c,d,e,f,g,h,i]),range(1,10))
##            return (sorted([a, b, c, d, e, f, g, h, i]) == list(range(1, 10)) and
##                 (a+b+c == d+e+f == g+h+i == a+d+g ==
##                 b+e+h == c+f+i == a+e+i == c+e+g == 15))
##
##        ans = 0
##        for r in range(R-2):
##            for c in range(C-2):
##                if grid[r+1][c+1] != 5: continue  # optional skip
##                if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
##                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
##                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
##                    ans += 1
##        return ans