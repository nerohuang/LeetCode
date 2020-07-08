class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [];
        numSum = 0;
        for num in nums:
            numSum += num;
            result.append(numSum);
        return result;

#class Solution:
#    def runningSum(self, nums: List[int]) -> List[int]:
#        for i in range(1, len(nums)):
#            nums[i] += nums[i-1]
#        return nums