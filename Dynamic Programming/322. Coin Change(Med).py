import bisect;

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1);
        dp[0] = 0;
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1);
        return dp[amount] if dp[amount] != float('inf') else -1;

#思路：
#维护一个dp，长度为amount+1；
#dp[i]代表在钱剩下i的时候需要多少个硬币。
#我们先遍历所有硬币，因为有可能用到所有硬币。
#然后从硬币的数值再遍历到总共需要的钱
#意思是寻找在硬币面值到总数的范围每一个数
#然后dp[i]最小需要的硬币就是这个公式：
#dp[i] = min(dp[i], dp[i - coin] + 1)；
#这个公式意思就是比较dp[i]和dp[i -coin] + 1;
#dp[i - coin]表示在剩余i钱的时候，减去当前coin
#所剩下的钱所需要的硬币，而这时候要额外+1是表示
#如果用了这个coin，所以要在dp[i -coin]的情况下
#加上一个硬币。
#所以答案就是返回dp[amount];