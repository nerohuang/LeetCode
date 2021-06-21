class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3= len(s1), len(s2), len(s3)
        if(not (l1 + l2 == l3)):
            return False
        
        dp = [[True for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
        
        return dp[-1][-1]

# 思路
# 用dp做
# s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
#   Ø d b b c a
# Ø T F F F F F
# a T F F F F F
# a T T T T T F
# b F T T F T F
# c F F T T T T
# c F F F T F T
# 建立一个DP
# 其中 dp[i][j] 表示的是 s2 的前 i 个字符和 s1 的前 j 个字符是否匹配 s3 的前 i+j 个字符，
# 根据以上分析，可写出代码如下：
# dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i - 1 + j]) || (dp[i][j - 1] && s2[j - 1] == s3[j - 1 + i]);
# 这个思路是dp[i][j]一上一左判断是否有true，有true说明这个字符串可以被合法延续
# 当上面有true的时候，那么就是竖着延续下来，那么就是要对比s1是否能延续
# 当左边有true的时候，那么就是横着延续，那么就要对比s2是否能延续