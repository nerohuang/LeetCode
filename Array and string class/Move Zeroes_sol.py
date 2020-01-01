class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for non_zero in range(len(nums)):
            if nums[non_zero] != 0:
                nums[zero], nums[non_zero] = nums[non_zero], nums[zero]
                zero += 1