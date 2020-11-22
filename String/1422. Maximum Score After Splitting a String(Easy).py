class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0;
        if len(s) == 2:
            left = s[:1];
            right = s[1:];
            ans = max(ans, left.count("0") + right.count("1"))
        for i in range(len(s) - 1):
            left = s[:1 + i];
            right = s[1 + i:];
            ans = max(ans, left.count("0") + right.count("1"))
        
        return ans

#class Solution:
#    def maxScore(self, s: str) -> int:
#        zeroes = 0
#        ones = 0
#        for c in s:
#            if c == "1":
#                ones += 1
#        max_score = 0
#        for i in range(len(s)-1):
#            if s[i] == "0":
#                zeroes += 1
#            if s[i] == "1":
#                ones -= 1
#            max_score = max(max_score,zeroes + ones)
#        return max_score
#思路，先把所有1统计出来，然后一位一位的算就可以了
            