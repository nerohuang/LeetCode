class Solution:
    def countSubstrings(self, s: str) -> int:
        store = [];
        ans = 0;
        
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    ans += 1;
        
        return ans + 1


#class Solution:
#    def countSubstrings(self, s: str) -> int:
#        n = len(s)
#        ans = 0
#        def center(lo,hi):
#            c = 0
#            while lo >= 0 and hi < n:
#                if s[lo] != s[hi]:
#                    break
#                lo -= 1
#                hi += 1
#                c += 1
#            return c
#        
#        for i in range(n):
#            ans += center(i,i)
#            ans += center(i,i+1)
#        return ans

# 这是一个找substring回文总数的题目。。
# 所以只要知道找回文的方法然后加起来就是了
# 和第五题是一样的。就是一左一右往外扩张。
# 直到不是回文就break
