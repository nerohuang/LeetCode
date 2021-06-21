class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxNum = nums[0];
        maxLoc = 0;
        for i in range(1, len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i];
                maxLoc = i;
        return maxLoc

# 我是弱智
                