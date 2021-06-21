class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows, columns = (len(s), len(p))
        # Base conditions
        if rows == 0 and columns == 0:
            return True
        if columns == 0:
            return False
        # DP array
        dp = [[False for j in range(columns + 1)] for i in range(rows + 1)]
        # Since empty string and empty pattern are a match
        dp[0][0] = True
        # Deals with patterns containing *
        for i in range(2, columns + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        # For remaining characters
        for i in range(1, rows + 1):
            for j in range(1, columns + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif j > 1 and p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[rows][columns]

# dp， 也是 dp
# 定义一个二维的 DP 数组，其中 dp[i][j] 表示 s[0,i) 和 p[0,j) 是否 match

#                     c	      *	      a	      *	      b
#             0	      1	      2 	  3	      4	      5
#       0	TRUE	FALSE	TRUE	FALSE	TRUE	FALSE
#  a	1	FALSE	FALSE	FALSE	TRUE	TRUE	FALSE
#  a	2	FALSE	FALSE	FALSE	FALSE	TRUE	FALSE
#  b	3	FALSE	FALSE	FALSE	FALSE	FALSE	TRUE

# 然后会有三种情况：
# if p[j - 1] != '*' && (s[i - 1] == p[j - 1] || p[j - 1] == '.')：
# P[i][j] = P[i - 1][j - 1]
# if p[j - 1] == '*' and the pattern repeats for 0 times;
# P[i][j] = P[i][j - 2]
# if p[j - 1] == '*' and the pattern repeats for at least 1 times.
# P[i][j] = P[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.')

# https://leetcode.com/problems/regular-expression-matching/discuss/5684/c-on-space-dp
# https://redquark.org/leetcode/0010-regular-expression-matching/