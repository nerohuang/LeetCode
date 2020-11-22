class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        count = 0;
        for word in sentence.split(" "):
            try:
                if word.find(searchWord) == 0:
                    return count + 1;
            except:
                count += 0;
            count += 1;
        return -1