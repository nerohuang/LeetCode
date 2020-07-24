class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        minimum  = prices[0];
        if len(prices) < 2:
            return 0;
        ans = 0;
        for i in range(1, len(prices)):
            if minimum > prices[i]:
                minimum = prices[i];
            elif prices[i] > minimum + fee:
                ans += prices[i] - minimum - fee;
                minimum = prices[i] - fee;
        return ans;

#greed