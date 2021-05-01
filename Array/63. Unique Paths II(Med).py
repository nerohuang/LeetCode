class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0;
        path = [[0] * (len(obstacleGrid[0]) + 1) for _ in range(len(obstacleGrid) + 1)]
        path[1][1] = 1;
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] != 1:
                    path[i + 1][j + 1] = path[i][j + 1] + path[i + 1][j] + path[i + 1][j + 1];
                    
        return path[-1][-1]

# 思路：
# 和前面那个其实是差不多的， 唯一差别是多了个挡路石
# 挡了路的怎么处理？如果没有东西挡的话第一行第一列的每一个节点都是1
# 那如果挡了，那么表示从那个挡路的节点开始之后都去不了了，都是0
# 然后就和前一个没挡路的算法是一样的
# path[i + 1][j + 1] = path[i][j + 1] + path[i + 1][j]
# 当然也要判断中间有没有挡路的，如果有，那么直接那个节点为0伺候