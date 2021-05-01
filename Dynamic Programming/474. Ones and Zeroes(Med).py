class Solution:
    def findMaxForm(self, S: List[str], M: int, N: int) -> int:
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for str in S:
            zeros = str.count("0")
            ones = len(str) - zeros
            # 什么情况？？？？
            for i in range(M, zeros - 1, -1):
                for j in range(N, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[M][N]

# 需要建立一个二维的DP数组，其中dp[i][j]表示有i个0和j个1时能
# 组成的最多字符串的个数，而对于当前遍历到的字符串，我们统计
# 出其中0和1的个数为zeros和ones，然后dp[i - zeros][j - ones]
# 表示当前的i和j减去zeros和ones之前能拼成字符串的个数，那么加上
# 当前的zeros和ones就是当前dp[i][j]可以达到的个数，我们跟其原
# 有数值对比取较大值即可，所以递推式如下：

# dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1);