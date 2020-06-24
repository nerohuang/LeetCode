class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortNums = sorted(nums);
        start = len(nums);
        end = 0;
        if nums == sortNums:
            return 0;
        else:
            for i in range(len(nums)):
                if nums[i] != sortNums[i]:
                    start = i;
                    break;
            for i in range(len(nums)):
                if nums[::-1][i] != sortNums[::-1][i]: ##[::-1]会慢很多很多
                    end = len(nums) - i;
                    break; 
            return (end - start);
                

##class Solution:
##    def findUnsortedSubarray(self, nums: List[int]) -> int:
##        l=len(nums)
##        s=sorted(nums)
##        left = l
##        for i in range(l):
##            if s[i] != nums[i]:
##                left = i
##                break
##
##        right = 0
##        for i in range(l-1, 0, -1):
##            if s[i] != nums[i]:
##                right = i
##                break
##        return right - left + 1 if right > left else 0
##

##def findUnsortedSubarray(self, nums):
##        is_same = [a == b for a, b in zip(nums, sorted(nums))]
##        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)