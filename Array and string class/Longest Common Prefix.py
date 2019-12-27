class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        if strs == ['']:
            return result
        if strs == []:
            return result
        short_str = min(strs, key=len)
        count = 0
        for i in range(len(short_str)):
            for word in strs:
                if short_str[i] == word[i]:
                    count = count + 1
            if count == len(strs):
                result = result + short_str[i]
                count = 0
            else:
                break
        return result
        