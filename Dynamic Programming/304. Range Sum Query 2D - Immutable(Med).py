class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)];
        
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                self.dp[i][j] = self.dp[i][j - 1] + self.dp[i - 1][j] + matrix[i - 1][j - 1] - self.dp[i - 1][j - 1];

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        return self.dp[row2][col2] - self.dp[row2][col1-1] - self.dp[row1-1][col2] + self.dp[row1-1][col1-1]

#dp思路:
#建立一个dp数组，dp[i][j]表示在[i][j]这个位置的累加值
#怎么累加呢？
#dp[i][j] = dp[i][j - 1] + dp[i - 1][j] + matrix[i - 1][j - 1] - dp[i - 1][j - 1];
#先用之前的累加值再加上[i][j]上的数字:
#dp[i][j - 1] + dp[i - 1][j] + matrix[i - 1][j - 1]
#然后因为dp[i][j]被计算了两次（dp[i][j - 1] + dp[i - 1][j]）
#所以要减去一次。
#当要求当前区域的时候：
#dp[row2 + 1][col2 + 1] - dp[row1][col2 + 1] - dp[row2 + 1][col1] + dp[row1][col1];
#就是以[row2][col2]上的整体累计值减去两块：
#[row1][col2]和[row2][col1]
#然后会发现[row1][col1]被减去了两次，要加回来一次。
#https://leetcode.com/problems/range-sum-query-2d-immutable/solution/