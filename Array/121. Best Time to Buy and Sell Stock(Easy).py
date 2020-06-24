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