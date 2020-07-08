class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0;
        for i in range(n):
            cur = start + 2 * i;
            ans ^= cur;
        return ans;
    
#class Solution:
#    def xorOperation(self, n: int, start: int) -> int:
#        j = start
#        for i in range(n-1):
#            j = j ^ (start + 2*(i+1))
#        return j