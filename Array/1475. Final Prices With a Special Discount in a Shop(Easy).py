class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = [];
        j = 0;
        for i in range(len(prices)):
            j = i + 1;
            while j < len(prices):
                if prices[i] >= prices[j]:
                    result.append(prices[i] - prices[j]);
                    break;
                j += 1;
            if j == len(prices):
                result.append(prices[i]);
        return result;

#class Solution:
#    def finalPrices(self, prices: List[int]) -> List[int]:
#        for i in range(len(prices)-1):
#            for j in range (i+1, len(prices)):
#                key = prices[j]
#                if key <= prices[i]:
#                    prices[i] = prices[i] - key
#                    break
#        return prices

#class Solution:
#    def finalPrices(self, prices: List[int]) -> List[int]:
#        lenlist = len(prices)
#        res = []
#        for i in range(lenlist):
#            flagset = 0
#            for j in range(i+1, lenlist):
#                if(prices[i] >= prices[j]):
#                    res.append(prices[i]-prices[j])
#                    flagset = 1
#                    break
#            if(j == lenlist-1 and flagset == 0):
#                res.append(prices[i])
#        print(res)
#        return res