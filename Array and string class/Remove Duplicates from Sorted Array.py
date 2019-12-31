class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        o_len = len(nums)
        i = 0
        j = 1
        while j < o_len:
            if nums[i] == nums[j]:
                del nums[j]
                o_len -= 1
            else:
                i += 1
                j = i + 1
        return len(nums)