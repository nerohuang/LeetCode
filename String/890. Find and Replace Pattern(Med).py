class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = [];
        if len(pattern) == 1:
            return words
        
        wordSize = len(pattern)
            
        for word in words:
            newSet = {}
            CharCount = []
            count = 0
            for i in range(wordSize):
                if newSet.get(pattern[i], "") == "" and word[i] not in CharCount:
                    newSet[pattern[i]] = word[i]
                    CharCount.append(word[i])
                    count += 1
                elif newSet.get(pattern[i], "") != word[i]:
                    break
                else:
                    count += 1
            if count == wordSize:
                ans.append(word)

                
        return ans



#class Solution:
#    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
#        res = []
#    
#        def match(word, pattern):
#            dir = {}
#            for w, p in zip(word, pattern):
#                if w not in dir:
#                    if p in dir.values():
#                        return False
#                    dir[w] = p
#                else:
#                    if dir[w] != p:
#                        return False
#            return True
#
#        for w in words:
#            if match(w, pattern):
#                res.append(w)
#        return res


# 思路：
# 其实就是对对碰，我的思路是就是一一对应
# 建立一个dict，然后pattern的字母作为key，而相对应位置的字符就作为value
# 当pattern在dict里面还没建立的时候，就建立他并且将value定位为word相
# 对应位置的字符，但如果这个对应的字符之前出现过，那么就出错了，返回false
# 所以我还建立了一个charCount专门记录哪些word的字符已经处理过了
# 然后count记录进行到第几位
# 如果这个patter的字符在之前已经处理过了而不能和之前存储的相对应的word
# 字符相等，那么就break跳出
# 最后比较长度，如果长度一样那么加入答案

# 下面有个稍微快一点的算法思路是一样的
# 用word 和 pattern相对应
# 如果word的字符没在dict里面，但是patter的字符已经出现在了
# dict的values里面，那么就返回错，如果没有，那么dict[w] = p
# 如果word的字符作为key出现在dict里面了，然后dict【w】的
# value却不是p，那就返回false
# 其实是一个意思