class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split( )[::-1]
        result = ' '.join(split) 
        return result