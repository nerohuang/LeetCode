class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0;
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2;
            else:
                i += 1;
        return True if i == len(bits) - 1 else False;

##class Solution:
##    def isOneBitCharacter(self, bits: List[int]) -> bool:
##        if not bits:
##            return False
##        
##        n = len(bits)
##        index = 0 
##        while index < n:
##            if index == n-1:
##                return True 
##            if bits[index] == 1:
##                index +=2
##            else:
##                index +=1 
##        return False