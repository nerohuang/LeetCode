class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0;
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxprofit += prices[i] - prices[i - 1];
        return maxprofit
# 思路
# 贪心，然后这次先比上一次差别在于可以连续买卖
# 那么可以连续买卖那么我们就不用找最高点和最低点了
# 可以把最高最低的卖出买入拆成中途无数次买入卖出
# 所以只要比较一前一后，只要前比后，就买入卖出一次
# 累计profit就可以了