class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(B) - sum(A)) / 2;
        for num in A:
            if (num + diff) in B:
                return[num, num + diff];

##class Solution:
##    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
##        diff = (sum(B) - sum(A)) / 2;
##        BSet = set(B); #set 查询更快
##        for num in A:
##            if (num + diff) in BSet:
##                return[num, num + diff];