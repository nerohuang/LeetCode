class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def toDict(word):
            newDict = {};
            for char in word:
                if char not in newDict:
                    newDict[char] = 1;
                else:
                    newDict[char] += 1;
            return newDict;
        
        
        ans = 0;
        charsDict = toDict(chars);
        for word in words:
            wordDict = toDict(word);
            curCount = 0;
            for char in wordDict:
                if (char in charsDict) and (wordDict[char] <= charsDict[char]):
                    curCount += wordDict[char];
                else:
                    break;
            if curCount == len(word):
                ans += curCount;
        return ans;

##class Solution:
##    def countCharacters(self, words: List[str], chars: str) -> int:
##        
##        result = 0
##        d = Counter(chars)
##        for word in words:
##            good = True
##            for char in word:
##                if (char not in d) or (word.count(char) > d[char]):
##                    good = False
##                    break
##            if good:
##                result += len(word)
##        return result