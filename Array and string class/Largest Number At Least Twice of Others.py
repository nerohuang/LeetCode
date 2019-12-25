class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            sort_num = sorted(nums)
            if (sort_num[-1] >= 2 * sort_num[-2]):
                for i,number in enumerate(nums):
                    if sort_num[-1] == number:
                        return i
            else:
                return -1