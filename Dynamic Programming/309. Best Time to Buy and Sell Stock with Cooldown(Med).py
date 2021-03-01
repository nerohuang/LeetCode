class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0;
        
        buy = [0 for _ in range(len(prices))];
        sell = [0 for _ in range(len(prices))];
        
        buy[0] -= prices[0]; 
        
        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], (sell[i - 2] if i > 1 else 0) - prices[i]);
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i]);
        
        return sell[-1]

#思路:
#大致上而言分為兩個陣列：
#sell
#buy
#其分別代表的意義是當天是否持有股票以及最大利益；sell[i]的最大利益有可能與前一天相同，亦或是於前一天買入股票並於當日賣出，因此：
#sell[i] = max(sell[i-1], buy[i-1] + prices[i])
#而buy[i]的最大利益有可能是當日無買入股票，亦或因為冷卻時間的關係，於前日賣出股票，並於今日買入股票，因此：
#buy[i] = max(buy[i-1], sell[i-2] - prices[i])