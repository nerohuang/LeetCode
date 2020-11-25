class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1;
        for i in range(len(s) - 1):
            try:
                last = len(s[i + 1:]) - s[i + 1:][::-1].index(s[i]) - 1;
            except:
                last = -1;
            if last != -1:
                ans = max(ans, last);
        return ans