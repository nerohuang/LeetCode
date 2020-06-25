class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxCount = 0 ;
        count = 1;
        if nums == []:
            return 0
        else:
            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    count += 1;
                else:
                    if count > maxCount:
                        maxCount = count;
                    count = 1;
        if count > maxCount:
            maxCount = count;
        return maxCount;





##class Solution:
##    def findLengthOfLCIS(self, nums: List[int]) -> int:
##        maxCount = 0 ;
##        index = 0;
##        for i in range(len(nums)):
##            if i >= 1 and nums[i - 1] >= nums[i]:
##                index = i;
##            maxCount = max(maxCount, i - index + 1)
##        return maxCount;