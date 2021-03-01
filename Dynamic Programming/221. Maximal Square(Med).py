class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))];
        for i in range(len(matrix[0])):
            dp[0][i] = int(matrix[0][i]);
        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0]);
        
        ans = 1;
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if int(matrix[i][j]):
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1;
                    ans = max(ans, dp[i][j]);
                    
                    
        return ans*ans

#思路：
#维护一个DP，大小和matrix一样，先把原来matrix里面第一行第一列放进去
#然后开始判断和更新dp：
#当matrix[i][j]为1的时候，说明可以延伸，然后因为是正方形
#所以要看dp[i - 1][j], dp[i][j], dp[i][j - 1]里面的最小值然后+1
#表明在之前该左边上，左和左上的最小，含有1的长度的基础上+1；
#而matrix[i][j]为0的时候，就说明不可以延伸，并且会断掉
#以直接dp[i][j]为0