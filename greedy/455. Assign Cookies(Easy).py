class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        child = 0
        cookie = 0
        ans = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                cookie += 1
                child += 1
                ans += 1
            else:
                child += 1
                
                
        return ans

# 思路：
# 有啥给啥