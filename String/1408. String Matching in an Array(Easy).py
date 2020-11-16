class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        store = set();
        for i in range(len(words)):
            for j in range(len(words)):
                if len(words[i]) >= len(words[j]) and words[i] != words[j]:
                    if words[i].find(words[j]) != -1:
                        store.add(words[j])
        
        return list(store)

#class Solution:
#    def stringMatching(self, words: List[str]) -> List[str]:
#        res = []
#        words.sort(key=len)
#        for i, word in enumerate(words):
#            for k in range(i+1, len(words)):
#                if word in words[k]:
#                    res.append(word)
#                    break
#
#        return res