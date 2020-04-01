class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        returnStr=""
        if len(strs) == 0:
            return returnStr
        else:
        
            minLength= len(strs[0])
            for eachString in strs[1:]:
                if len(eachString)<minLength:
                    minLength=len(eachString)
                    
            compareString = strs[0][:minLength]

            print(compareString)

            for eachStr in strs:
                compareString = self.findPre(compareString,eachStr)
                if compareString=="": break
                    
            return compareString
                
    def findPre(self,src,tar):
        returnStr=""
        
        for eachLettersrc,eachLettertrg in zip(src,tar):
            if eachLettersrc==eachLettertrg:
                returnStr+=eachLettersrc
            else:
                break
                
        return returnStr