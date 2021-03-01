class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ");
        maxLen = len(max(words, key = lambda x:len(x)));
        for i in range(len(words)):
            if len(words[i]) < maxLen:
                words[i] = words[i] + " " * (maxLen - (len(words[i])));
        ans = [];
        for i in range(maxLen):
            curStr = "";
            for word in words:
                curStr += word[i];
            ans.append(curStr.rstrip())
        return ans;