class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        value = 0;
        count = 0
        result = [];
        for num in A:
            value = value*2 + num;
            if value % 5 == 0:
                result.append(True);
            else:
                result.append(False);
        return result;

##class Solution:
##    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
##        def nums(bits):
##            curr = 0
##            for bit in bits:
##                curr = (2 * curr + bit) % 5
##                yield curr
##                
##        return [num == 0 for num in nums(A)]