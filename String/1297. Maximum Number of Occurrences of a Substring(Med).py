class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        curAns = collections.defaultdict(int);
        for i in range(minSize, maxSize + 1):
            for j in range(len(s) - i + 1):
                curStr = s[j:j + i];
                count = collections.Counter(list(curStr));
                if len(count) <= maxLetters:
                    curAns[curStr] += 1;
        if curAns:
            return max(curAns.values());
        else:
            return 0

# 这是个暴力全搜索的方法
# 但其实仔细想一想。。他这个maxSzie根本没用
# 因为所有size大于minSize符合要求的话
# 那么他的长度为minSize的substring肯定也符合
# 所以其实只要遍历一遍minSize就行了。。
# 注意到解出现在size > minSize时，它内部满足
# 条件（独特字符数<maxLetters）的子串一定也
# 会出现在minSize的结果里，所以只需要遍历
# minSize就可以了。

#class Solution:
#    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
#        counts = {}
#        
#        for i in range(len(s)-minSize+1):
#            word = s[i:i + minSize]
#            
#            if word in counts:
#                counts[word] += 1
#            else:
#                if len(set(word)) <= maxLetters:
#                    counts[word] = 1
#            
#        return max(counts.values()) if len(counts) != 0 else 0