class Solution:
    def makeGood(self, s: str) -> str:
        ans = [s]
        def findStr(s):
            for i in range(1, len(s)):
                # find the first bad sub-string
                if s[i - 1] != s[i] and s[i - 1].lower() == s[i].lower():
                    ans.append(s[:i - 1] + s[i + 1:])
                    # make the rest string great
                    return findStr(s[:i - 1] + s[i + 1:])
        
        findStr(s)
        return ans[-1];

#思路：因为要连续两个相同字母且一个大写一个小写，所以只要是前后两个字母不相同但
#小写的时候相同就可以了，然后用递归全部找完。

#class Solution:
#    def makeGood(self, s: str) -> str:
#        stack=[]
#        for i in s:
#            if stack and stack[-1]==i.swapcase():
#                stack.pop()
#            else:
#                stack.append(i)
#        return "".join(stack)
#快速方法：用栈