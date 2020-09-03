class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        j = 0;
        curCost = 0;
        ans = 0;
        for i in range(len(s)):
            curCost += abs(ord(s[i]) - ord(t[i]));
            while curCost > maxCost and j <= i:
                curCost -= abs(ord(s[j]) - ord(t[j]));
                j += 1;
            ans = max(ans, i - j + 1);
        return ans;

#建立sliding window，先把当前窗口的cost累加，一旦累加超过了maxCost，就从最左边
#开始减去最左位的cost直到curCost少于maxCost或者最左边一位已经到了右边。
#答案就是最右位和最左位之差，然后求max
