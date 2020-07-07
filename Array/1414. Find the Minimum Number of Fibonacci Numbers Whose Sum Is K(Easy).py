class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        FibList = [1, 1];
        i = 2
        ans = 0;
        while FibList[-1] < k:
            FibList.append(FibList[i - 1] + FibList[i - 2]);
            i += 1;
        i = -1;
        while k != 0:
            if k >= FibList[i]:
                k -= FibList[i];
                ans += 1;
            i -= 1;
        return ans;

#from bisect import bisect
#
#class Solution:
#    def findMinFibonacciNumbers(self, k: int) -> int:
#        fibs_at_most = self.get_fibonacci_at_most(k)
#        count = 0
#        while k >= 1:
#            count += 1
#            k -= fibs_at_most[bisect(fibs_at_most, k) - 1]
#        return count
#
#    @staticmethod
#    def get_fibonacci_at_most(n: int) -> bool:
#        res = [1, 1]
#        while res[-1] < n:
#            res.append(res[-1] + res[-2])
#        return res