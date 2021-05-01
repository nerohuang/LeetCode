class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if len(p) <= 1:
            return len(p);
        count = defaultdict(int);
        maxLen = 1;
        count[p[0]] = 1;
        match = 'zabcdefghijklmnopqrstuvwxyz';
        
        for i in range(1, len(p)):
            if p[i - 1] + p[i] in match:
                maxLen += 1;
            else:
                maxLen = 1;
            
            count[p[i]] = max(count[p[i]], maxLen);
        return sum(count.values())
# 思路：
# 累计长度是个基础：
# 我们首先要找出里面有的字母，然后代表那个字母为结尾最长的substring
# 因为是substring所以不能有重复的，所以不必担心重复。
# 所以我们就可以开始遍历了。
# 如果p[i - 1] + p[i]在match里面，意思就是这个substring也是match
# 的substring。那么就可以延续长度，所以maxLen + 1；
# 然后开始比较以该字母为结尾的substring最长是多少。
# 然后把这些字母所得的长度相加就是答案。
# 我们看abcd这个字符串，以d结尾的子字符串有abcd, bcd, cd, d，
# 那么我们可以发现bcd或者cd这些以d结尾的字符串的子字符串都包含在abcd中