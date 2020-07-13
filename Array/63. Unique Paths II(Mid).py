class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        path = [];
        curLine = [];
        blockLoc = [];
        m = len(obstacleGrid);
        n = len(obstacleGrid[0]);
        blockInFirstLine = n + 1;
        blockInFirstCol = m + 1;
        if obstacleGrid[0][0] == 1:
            return 0;
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    if i == 0:
                        blockInFirstLine = min(j, blockInFirstLine);
                    if j == 0:
                        blockInFirstCol = min(i, blockInFirstCol);
                    blockLoc.append([i, j]);
                    obstacleGrid[i][j] = -1;
        for i in range(m):
            if i < blockInFirstCol:
                obstacleGrid[i][0] = 1;
        for i in range(n):
            if i < blockInFirstLine:
                obstacleGrid[0][i] = 1;
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != -1:
                    if obstacleGrid[i - 1][j] != -1 and obstacleGrid[i][j - 1] != -1:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1];
                    elif obstacleGrid[i - 1][j] == -1:
                        obstacleGrid[i][j] = obstacleGrid[i][j - 1];
                    elif obstacleGrid[i][j - 1] == -1:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j];
        return obstacleGrid[m - 1][n - 1] if obstacleGrid[m - 1][n - 1] != -1 else 0;


#class Solution:
#    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#        if len(obstacleGrid) == 0:
#            return 0
#        lst = [[0 for i in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
#        lst[0][0] = 1
#        for i in range(len(obstacleGrid)):
#            for j in range(len(obstacleGrid[0])):
#                if obstacleGrid[i][j] == 1:
#                    lst[i][j] = 0
#                else:
#                    if i - 1 >= 0:
#                        lst[i][j] += lst[i - 1][j]
#                    if j - 1 >= 0:
#                        lst[i][j] += lst[i][j - 1]
#        return lst[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]