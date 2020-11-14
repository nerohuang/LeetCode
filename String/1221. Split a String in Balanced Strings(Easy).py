class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lCount = 0;
        rCount = 0;
        ans = 0;
        for char in s:
            if char == "L":
                lCount += 1;
            if char == "R":
                rCount += 1;
            if lCount != 0 and lCount == rCount:
                ans += 1;
                lCount = 0;
                rCount = 0;
        
        return ans;