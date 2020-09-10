class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix);
        n = len(matrix[0]);
        ans = 0;
        count = [[0] * (n + 1) for _ in range(m + 1)];
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (matrix[i - 1][j - 1] == 1):
                    count[i][j] = 1 + min(count[i - 1][j - 1], count[i - 1][j], count[i][j - 1])
                    ans += count[i][j];
        return ans;

#思路：其实和矩阵寻找最终线路差不多，但区别在于就是寻找周围里面现存最小的然后加1
#但如果当前是0的话就不要进行判断因为只要存在0就要忽略。