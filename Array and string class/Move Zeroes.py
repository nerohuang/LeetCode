class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0 
        j = i + 1
        while i < len(nums):
            if nums[i] == 0 and j < len(nums):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j = i + 1
                else:
                    j += 1
            else:
                i += 1
                j = i + 1
        return nums