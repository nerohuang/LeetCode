class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = [];
        for i in range(0, len(nums) - 1, 2):
            for j in range(nums[i]):
                result.append(nums[i + 1]);
        return result;

##class Solution:
##    def decompressRLElist(self, nums: List[int]) -> List[int]:
##        result=[]
##        i, multiplier = 0,1
##        while (i < len(nums)):
##            if i % 2 == 0:
##                multiplier = nums[i]
##            else:
##                tmp = (str(nums[i]) + ',') * multiplier
##                result.append(tmp[:-1])
##            i += 1
##        return result