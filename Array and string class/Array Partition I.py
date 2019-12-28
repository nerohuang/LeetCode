class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        print(nums)
        i = 0
        j = len(nums) - 2
        while i < j:
            result = result + nums[i] + nums[j]
            i += 2
            j -= 2
        if (len(nums) / 2) % 2 == 1:
            result = result + nums[i]
        return result