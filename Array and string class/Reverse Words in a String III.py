class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        split = s.split()
        for i in range(len(split)):
            split[i] = split[i][::-1]
        result = ' '.join(split) 
        return result