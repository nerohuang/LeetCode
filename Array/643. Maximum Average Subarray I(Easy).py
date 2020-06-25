class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[:k]);
        curSum = sum(nums[:k]);
        for i in range(0, len(nums) - k):
            if maxSum < (curSum - nums[i] + nums[i + k]):
                maxSum = curSum - nums[i] + nums[i + k];
            curSum = curSum - nums[i] + nums[i + k]
        return maxSum/k;

##class Solution:
##    def findMaxAverage(self, nums: List[int], k: int) -> float:
##        
##        res = cur = 0
##        for i in range(len(nums) - k):
##            cur = cur - nums[i] + nums[i + k]
##            if cur > res:
##                res = cur
##        return (sum(nums[:k]) + res) / k
        