class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word2Str = "".join(word2);
        for word in word1:
            if word in word2Str:
                index = word2Str.find(word);
                word2Str = word2Str[:index] + word2Str[index + len(word):];
        if word2Str == "":
            return True
        else:
            return False