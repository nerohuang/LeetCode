class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)];
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        
        return len(word1) + len(word2) - 2 * dp[len(word1)][len(word2)];

# 一个典型的DP问题
# 其实就是寻找最长公共子序列的问题
# 建立一个dp[i][j]表示 word1 的前i个字符和 word2 
# 的前j个字符组成的两个单词的最长公共子序列的长度。
# 首先来考虑 dp[i][j] 和 dp[i-1][j-1] 之间的关系，
# 可以发现，如果当前的两个字符相等，那么 
# dp[i][j] = dp[i-1][j-1] + 1
# 如果不相等，要错位相比：
# 比如就拿题目中的例子来说，"sea" 和 "eat"，当比较
# 第一个字符，发现 's' 和 'e' 不相等，下一步就要错
# 位比较啊，比较 sea 中第一个 's' 和 eat 中的 'a'，
# sea 中的 'e' 跟 eat 中的第一个 'e' 相比，这样 
# dp[i][j] 就要取 dp[i-1][j] 跟 dp[i][j-1] 中的较
# 大值了，最后求出了最大共同子序列的长度，就能直接算
# 出最小步数了，