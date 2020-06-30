class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans= 0 ;
        store = {};
        for num in time:
            if -num % 60 in store:
                ans += store[-num % 60];
                if num % 60 in store:
                    store[num % 60] += 1;
                else:
                    store[num % 60] = 1;
            else:
                if num % 60 in store:
                    store[num % 60] += 1;
                else:
                    store[num % 60] = 1;
        return ans;

##class Solution:
##    def numPairsDivisibleBy60(self, time: List[int]) -> int:
##        result = 0
##        dict = {}
##        for t in time:
##            v = t % 60
##            if v in dict:
##                dict[v] = dict[v] + 1
##            else:
##                dict[v] = 1
##        for k in dict:
##            if k == 0 or k == 30:
##                result = result + dict[k] * (dict[k] - 1) // 2
##            elif k < 30:
##                if (60 - k) in dict:
##                    result = result + dict[k] * dict[60 - k]
##        return result