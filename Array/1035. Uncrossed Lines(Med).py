class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B);
        dp = [[0] * (n + 1) for _ in range(m + 1)] 
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                
        return dp[-1][-1]

#最长公共子序列
#感觉和在一个矩阵中找到从起点到终点的所有路径相似。
#比如[1,4,2],[1,2,4], 先构造一个DP table：
#   \ | 0 | 1  2  3
#   ---------------
#   0 | " | 1  4  2
#   ---------------
#   1 | 1 | 1  1  1
#   2 | 2 | 1  1  2
#   3 | 4 | 1  2  2
#可以得出这样一个table，然后找到最右下角的那个就是最大的
#详情可以看
#https://leetcode-cn.com/problems/longest-common-subsequence/solution/dong-tai-gui-hua-zhi-zui-chang-gong-gong-zi-xu-lie/