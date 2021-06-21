class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprofit = 999999999999999999999999999;
        maxprofit = 0;
        for num in prices:
            if num < minprofit:
                minprofit = num;
            elif num - minprofit > maxprofit:
                maxprofit = num - minprofit;
        return maxprofit;
# 贪心：
# 思路：
# 因为只有一次买卖，所以就要找出最低价和最高价
# 用比较就可以实现
# 通过对比实现找出最低价，如果当前数字比最低价
# 高，那么就尝试卖出（减法）看看是不是比之前
# 的最高收益高，如果是就更新