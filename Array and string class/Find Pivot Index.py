class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = sum(nums)
        result = -1
        if (len(nums) != 0):
            record = 0
            for i in range (len(nums)):
                record += nums[i]
                if (record == (sums - record + nums[i])):
                    result = i
                    break
        else:
            result = -1
        return result