class Solution:
    def climbStairs(self, n: int) -> int:
        step = [1, 2];
        for i in range(2, n):
            step.append(step[-1] + step[-2]);
        return step[n - 1]

#思路：
#假设梯子有n层，那么如何爬到第n层呢，因为每次只能爬1或2步，
#那么爬到第n层的方法要么是从第 n-1 层一步上来的，要不就是
#从 n-2 层2步上来的，而这dp[n-1]和dp[n-2]的解决方法是不重复的
#dp[n] = dp[n-1] + dp[n-2]。
#如果是一次最多上三层那么就是dp[n-1]+dp[n-2]+dp[n-3];